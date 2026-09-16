from __future__ import annotations

import numpy as np

from .base import MapGenerator
from ..occupancy_grid import OccupancyGrid, FREE


class EmptyMapGenerator(MapGenerator):

    def __init__(
        self,
        width: int,
        height: int,
        resolution: float = 1.0,
        name: str = "empty",
    ):
        self.width = width
        self.height = height
        self.resolution = resolution
        self.name = name

    def generate(self) -> OccupancyGrid:

        data = np.full(
            (self.height, self.width),
            FREE,
            dtype=np.int8,
        )

        return OccupancyGrid(
            data=data,
            resolution=self.resolution,
            name=self.name,
        )
