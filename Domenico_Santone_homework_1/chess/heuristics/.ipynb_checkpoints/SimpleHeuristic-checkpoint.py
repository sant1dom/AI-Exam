import chess
import random
from .AbstractHeuristic import AbstractHeuristic


class SimpleHeuristic(AbstractHeuristic):
    """
        SimpleHeuristic is a heuristic that prioritizes moves that reduce the number of other player's pieces on the board.
    """
    def __init__(self):
        pass

    def h0(self, state: chess.Board):
        # number of white pieces - number of black pieces
        white_pieces = 0
        black_pieces = 0
        for piece in state.piece_map().values():
            if piece.color == chess.WHITE:
                white_pieces += 1
            else:
                black_pieces += 1
        return white_pieces - black_pieces

    def hl(self, state: chess.Board, move, depth):
        if depth == 0:
            return self.h0(state), move
        if state.turn == chess.WHITE:
            max_eval = -100000
            best_move = None
            neighbours = random.sample(list(state.legal_moves), len(list(state.legal_moves)))
            for neighbour in neighbours:
                evaluation = self.hl(state, neighbour, depth - 1)[0]
                max_eval = max(max_eval, evaluation)
                if max_eval == evaluation:
                    best_move = neighbour
            return [max_eval, best_move]
        else:
            min_eval = 100000
            best_move = None
            neighbours = random.sample(list(state.legal_moves), len(list(state.legal_moves)))
            for neighbour in neighbours:
                evaluation = self.hl(state, neighbour, depth - 1)[0]
                min_eval = min(min_eval, evaluation)
                if min_eval == evaluation:
                    best_move = neighbour
            return [min_eval, best_move]
