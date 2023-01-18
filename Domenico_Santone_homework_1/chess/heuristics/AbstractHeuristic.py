from abc import ABC, abstractmethod
from typing import Any


class AbstractHeuristic(ABC):
    """
        AbstractHeuristic is an abstract class that defines the interface for all heuristic functions.
    """
    def __init__(self):
        pass

    @abstractmethod
    def evaluate(self, state: Any):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}"
