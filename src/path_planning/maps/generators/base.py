from __future__ import annotations

from abc import ABC, abstractmethod

from ..occupancy_grid import OccupancyGrid


class MapGenerator(ABC):
    """
    Base interface for all static map generators.
    """

    @abstractmethod
    def generate(self) -> OccupancyGrid:
        """
        Generate a map.
        """
        raise NotImplementedError
