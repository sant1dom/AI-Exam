from heuristics.SimpleHeuristic import AbstractHeuristic
import chess
import random


class Agent:
    def __init__(self, heuristic: AbstractHeuristic, depth: int = 1):
        self.heuristic: AbstractHeuristic = heuristic
        self.depth = depth

    def play(self, board):
        return self.minimax(board, None, self.depth, float('-inf'), float('inf'), True)[1]

    def minimax(self, state, move, depth, alpha, beta, turn):
        if depth == 0:
            return self.heuristic.evaluate(state), move
        if turn:
            max_eval = -100000
            best_move = None
            neighbours = random.sample(list(state.legal_moves), len(list(state.legal_moves)))
            for neighbour in neighbours:
                state.push(neighbour)
                evaluation = self.minimax(state, neighbour, depth - 1, alpha, beta, not turn)[0]
                state.pop()
                max_eval = max(max_eval, evaluation)
                alpha = max(alpha, max_eval)
                if max_eval == evaluation:
                    best_move = neighbour
                if beta <= alpha:
                    break
            return [max_eval, best_move]
        else:
            min_eval = 100000
            best_move = None
            neighbours = random.sample(list(state.legal_moves), len(list(state.legal_moves)))
            for neighbour in neighbours:
                state.push(neighbour)
                evaluation = self.minimax(state, neighbour, depth - 1, alpha, beta, not turn)[0]
                state.pop()
                min_eval = min(min_eval, evaluation)
                beta = min(beta, min_eval)
                if min_eval == evaluation:
                    best_move = neighbour
                if beta <= alpha:
                    break
            return [min_eval, best_move]

