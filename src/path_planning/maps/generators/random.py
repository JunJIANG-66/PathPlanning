from __future__ import annotations

from typing import Optional

import numpy as np

from .base import MapGenerator
from ..occupancy_grid import OccupancyGrid, FREE, OCCUPIED


class RandomMapGenerator(MapGenerator):
    """Generate a random occupancy grid."""

    def __init__(
        self,
        width: int,
        height: int,
        obstacle_probability: float = 0.2,
        resolution: float = 1.0,
        seed: Optional[int] = None,
        name: str = "random",
    ):
        if width <= 0:
            raise ValueError("width must be greater than zero.")

        if height <= 0:
            raise ValueError("height must be greater than zero.")

        if resolution <= 0:
            raise ValueError("resolution must be greater than zero.")

        if not 0.0 <= obstacle_probability <= 1.0:
            raise ValueError(
                "obstacle_probability must be between 0 and 1."
            )

        self.width = width
        self.height = height
        self.obstacle_probability = obstacle_probability
        self.resolution = resolution
        self.seed = seed
        self.name = name

    def generate(self) -> OccupancyGrid:
        """Generate and return a random occupancy grid."""

        rng = np.random.default_rng(self.seed)

        random_values = rng.random(
            (self.height, self.width)
        )

        data = np.where(
            random_values < self.obstacle_probability,
            OCCUPIED,
            FREE,
        ).astype(np.int8)

        return OccupancyGrid(
            data=data,
            resolution=self.resolution,
            name=self.name,
        )
