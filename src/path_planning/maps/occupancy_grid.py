from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Tuple, Union

import numpy as np


FREE = 0
OCCUPIED = 100
UNKNOWN = -1


@dataclass
class OccupancyGrid:

    data: np.ndarray
    resolution: float = 1.0
    origin: Tuple[float, float, float] = (0.0, 0.0, 0.0)
    name: str = "map"

    def __post_init__(self):
        if self.data.ndim != 2:
            raise ValueError(
                "Occupancy grid data must be a 2D array."
            )

        if self.resolution <= 0:
            raise ValueError(
                "Resolution must be greater than zero."
            )

        self.data = np.asarray(
            self.data,
            dtype=np.int8,
        )

    @property
    def height(self) -> int:
        return self.data.shape[0]

    @property
    def width(self) -> int:
        return self.data.shape[1]

    @property
    def shape(self) -> Tuple[int, int]:
        return self.data.shape

    @property
    def size(self) -> Tuple[int, int]:
        return self.width, self.height

    @property
    def world_width(self) -> float:
        return self.width * self.resolution

    @property
    def world_height(self) -> float:
        return self.height * self.resolution

    def is_free(
        self,
        row: int,
        col: int,
    ) -> bool:
        return self.data[row, col] == FREE

    def is_occupied(
        self,
        row: int,
        col: int,
    ) -> bool:
        return self.data[row, col] == OCCUPIED

    def is_unknown(
        self,
        row: int,
        col: int,
    ) -> bool:
        return self.data[row, col] == UNKNOWN

    def grid_to_world(
        self,
        row: int,
        col: int,
    ) -> Tuple[float, float]:

        x = (
            self.origin[0]
            + (col + 0.5) * self.resolution
        )

        y = (
            self.origin[1]
            + (row + 0.5) * self.resolution
        )

        return x, y

    def world_to_grid(
        self,
        x: float,
        y: float,
    ) -> Tuple[int, int]:

        col = int(
            (x - self.origin[0])
            / self.resolution
        )

        row = int(
            (y - self.origin[1])
            / self.resolution
        )

        return row, col

    def save(
        self,
        path: Union[str, Path],
    ) -> None:

        path = Path(path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        np.save(
            path,
            self.data,
        )

    @classmethod
    def load(
        cls,
        path: Union[str, Path],
        resolution: float = 1.0,
        origin: Tuple[
            float,
            float,
            float,
        ] = (0.0, 0.0, 0.0),
        name: str = "map",
    ) -> "OccupancyGrid":

        data = np.load(path)

        return cls(
            data=data,
            resolution=resolution,
            origin=origin,
            name=name,
        )
