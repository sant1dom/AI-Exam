from .AbstractHeuristic import AbstractHeuristic
import chess
import chess.polyglot


class CheckHeuristic(AbstractHeuristic):
    """
        CheckHeuristic is a heuristic that prioritizes moves that put the opponent in check.
    """
    def __init__(self):
        pass

    def evaluate(self, state):
        # this heuristic should prioritize moves that put the opponent in check
        # if the opponent is already in check, prioritize moves that checkmate
        white_pieces = 0
        black_pieces = 0
        value_dict = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 100}
        for piece in state.piece_map().values():
            if piece.color == chess.WHITE:
                white_pieces += value_dict[piece.piece_type]
            else:
                black_pieces += value_dict[piece.piece_type]
        if state.turn == chess.WHITE:
            if state.is_check():
                if state.is_checkmate():
                    return 100000
                else:
                    return 1000
            else:
                return white_pieces - black_pieces
        else:
            if state.is_check():
                if state.is_checkmate():
                    return -100000
                else:
                    return -1000
            else:
                return black_pieces - white_pieces