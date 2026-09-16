from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np


FREE = 0
OCCUPIED = 100
UNKNOWN = -1


@dataclass
class OccupancyGrid:
    """
    2D occupancy grid.

    data:
        2D numpy array with values:
            0   -> free
            100 -> occupied
            -1  -> unknown
    """

    data: np.ndarray
    resolution: float = 1.0
    origin: tuple[float, float, float] = (0.0, 0.0, 0.0)
    name: str = "map"

    def __post_init__(self):
        if self.data.ndim != 2:
            raise ValueError("Occupancy grid data must be a 2D array.")

        if self.resolution <= 0:
            raise ValueError("Resolution must be greater than zero.")

        self.data = np.asarray(self.data, dtype=np.int8)

    @property
    def height(self) -> int:
        return self.data.shape[0]

    @property
    def width(self) -> int:
        return self.data.shape[1]

    @property
    def shape(self) -> tuple[int, int]:
        return self.data.shape

    @property
    def size(self) -> tuple[int, int]:
        return self.width, self.height

    @property
    def world_width(self) -> float:
        return self.width * self.resolution

    @property
    def world_height(self) -> float:
        return self.height * self.resolution

    def is_free(self, row: int, col: int) -> bool:
        return self.data[row, col] == FREE

    def is_occupied(self, row: int, col: int) -> bool:
        return self.data[row, col] == OCCUPIED

    def is_unknown(self, row: int, col: int) -> bool:
        return self.data[row, col] == UNKNOWN

    def grid_to_world(
        self,
        row: int,
        col: int,
    ) -> tuple[float, float]:
        """
        Convert grid coordinates to world coordinates.

        Returns the center of the grid cell.
        """

        x = self.origin[0] + (col + 0.5) * self.resolution
        y = self.origin[1] + (row + 0.5) * self.resolution

        return x, y

    def world_to_grid(
        self,
        x: float,
        y: float,
    ) -> tuple[int, int]:
        """
        Convert world coordinates to grid coordinates.
        """

        col = int((x - self.origin[0]) / self.resolution)
        row = int((y - self.origin[1]) / self.resolution)

        return row, col

    def save(self, path: str | Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)

        np.save(path, self.data)

    @classmethod
    def load(
        cls,
        path: str | Path,
        resolution: float = 1.0,
        origin: tuple[float, float, float] = (0.0, 0.0, 0.0),
        name: str = "map",
    ) -> "OccupancyGrid":

        data = np.load(path)

        return cls(
            data=data,
            resolution=resolution,
            origin=origin,
            name=name,
        )
