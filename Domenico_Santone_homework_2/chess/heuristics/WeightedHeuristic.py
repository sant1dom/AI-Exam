import chess
import chess.polyglot
from .AbstractHeuristic import AbstractHeuristic


class WeightedHeuristic(AbstractHeuristic):
    """
        WeightedHeuristic is a heuristic that evaluates the state of the board by counting the number of pieces of each color and weighting them by their value.
    """
    def __init__(self):
        pass

    def evaluate(self, state: chess.Board):
        # number of white pieces - number of black pieces weighted by piece value
        white_pieces = 0
        black_pieces = 0
        value_dict = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 100}
        for piece in state.piece_map().values():
            if piece.color == chess.WHITE:
                white_pieces += value_dict[piece.piece_type]
            else:
                black_pieces += value_dict[piece.piece_type]
        return white_pieces - black_pieces

