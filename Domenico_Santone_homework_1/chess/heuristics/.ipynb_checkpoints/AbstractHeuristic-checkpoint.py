from abc import ABC, abstractmethod
from typing import Any


class AbstractHeuristic(ABC):
    """
        AbstractHeuristic is an abstract class that defines the interface for all heuristic functions.
    """
    def __init__(self):
        pass

    @abstractmethod
    def h0(self, state: Any):
        pass

    @abstractmethod
    def hl(self, state: Any, move: Any, depth: Any):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}"
