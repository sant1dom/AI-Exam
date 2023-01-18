from .AbstractHeuristic import AbstractHeuristic
from chessmate.engines import ScholarsMate


class TryHeuristic(AbstractHeuristic):
    """
        StockFishHeuristic is a heuristic that prioritizes moves that reduce the number of other player's pieces on the board.
    """

    def h0(self, state):
        # Use the ScholarsMate engine to evaluate the state of the board
        return ScholarsMate().evaluate(state)

    def __repr__(self):
        return f"{self.__class__.__name__}"
