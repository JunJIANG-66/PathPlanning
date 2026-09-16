from __future__ import annotations

import numpy as np

from .base import MapGenerator
from ..occupancy_grid import OccupancyGrid, FREE, OCCUPIED


class WarehouseMapGenerator(MapGenerator):
    """Generate a structured warehouse-style occupancy grid."""

    def __init__(
        self,
        width: int,
        height: int,
        shelf_width: int = 3,
        shelf_length: int = 20,
        aisle_width: int = 4,
        shelf_spacing: int = 8,
        border_width: int = 1,
        resolution: float = 1.0,
        name: str = "warehouse",
    ):
        if width <= 0:
            raise ValueError("width must be greater than zero.")

        if height <= 0:
            raise ValueError("height must be greater than zero.")

        if shelf_width <= 0:
            raise ValueError("shelf_width must be greater than zero.")

        if shelf_length <= 0:
            raise ValueError("shelf_length must be greater than zero.")

        if aisle_width <= 0:
            raise ValueError("aisle_width must be greater than zero.")

        if shelf_spacing <= 0:
            raise ValueError("shelf_spacing must be greater than zero.")

        if border_width < 0:
            raise ValueError("border_width cannot be negative.")

        if resolution <= 0:
            raise ValueError("resolution must be greater than zero.")

        if 2 * border_width >= width:
            raise ValueError(
                "border_width is too large for the map width."
            )

        if 2 * border_width >= height:
            raise ValueError(
                "border_width is too large for the map height."
            )

        self.width = width
        self.height = height
        self.shelf_width = shelf_width
        self.shelf_length = shelf_length
        self.aisle_width = aisle_width
        self.shelf_spacing = shelf_spacing
        self.border_width = border_width
        self.resolution = resolution
        self.name = name

    def generate(self) -> OccupancyGrid:
        """Generate and return a warehouse occupancy grid."""

        data = np.full(
            (self.height, self.width),
            FREE,
            dtype=np.int8,
        )

        self._add_border(data)
        self._add_shelves(data)

        return OccupancyGrid(
            data=data,
            resolution=self.resolution,
            name=self.name,
        )

    def _add_border(self, data: np.ndarray) -> None:
        """Add a solid obstacle border around the map."""

        b = self.border_width

        if b == 0:
            return

        data[:b, :] = OCCUPIED
        data[-b:, :] = OCCUPIED
        data[:, :b] = OCCUPIED
        data[:, -b:] = OCCUPIED

    def _add_shelves(self, data: np.ndarray) -> None:
        """Add regularly spaced warehouse shelves."""

        b = self.border_width

        x = b + self.aisle_width

        while x + self.shelf_width <= self.width - b:

            y = b + self.aisle_width

            while y + self.shelf_length <= self.height - b:

                x_end = x + self.shelf_width
                y_end = y + self.shelf_length

                data[y:y_end, x:x_end] = OCCUPIED

                y += self.shelf_length + self.aisle_width

            x += self.shelf_width + self.shelf_spacing
