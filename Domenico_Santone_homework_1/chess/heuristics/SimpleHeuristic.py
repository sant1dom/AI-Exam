import chess
import chess.polyglot
from .AbstractHeuristic import AbstractHeuristic


class SimpleHeuristic(AbstractHeuristic):
    """
        SimpleHeuristic is a heuristic that prioritizes moves that reduce the number of other player's pieces on the board.
    """
    def __init__(self):
        pass

    def evaluate(self, state: chess.Board):
        # number of white pieces - number of black pieces
        white_pieces = 0
        black_pieces = 0
        for piece in state.piece_map().values():
            if piece.color == chess.WHITE:
                white_pieces += 1
            else:
                black_pieces += 1
        return white_pieces - black_pieces
