import random
import math
from Agent import Agent
from heuristics.AbstractHeuristic import AbstractHeuristic


class BestLAgent(Agent):
    def __init__(self, heuristic: AbstractHeuristic, depth=1, k=1):
        super().__init__(heuristic, depth)
        self.k = k
        self.best_moves = []

    def play(self, board):
        self.minimaxBestK(board, [], math.ceil(self.depth/2), float('-inf'), float('inf'), True)
        list_of_moves = []
        for state in self.best_moves:
            for move in state[1]:
                board.push(move)
            list_of_moves.append((self.minimax(board, None, math.floor(self.depth/2), float('-inf'), float('inf'), True)[0], state[1][0]))
            for move in state[1]:
                board.pop()
        if self.depth % 2 == 0:
            self.best_moves.clear()
            return max(list_of_moves, key=lambda x: x[0])[1]
        else:
            self.best_moves.clear()
            return min(list_of_moves, key=lambda x: x[0])[1]

    def minimaxBestK(self, state, moves, depth, alpha, beta, turn):
        # A Version of the minimax algorithm that olny evaluates the best subtrees of the game tree
        # and returns the best moves to get to those subtrees. It saves the best moves in the
        # self.best_moves list associated with the evaluation of the subtree.
        if depth == 0:
            evaluation = self.heuristic.evaluate(state)
            if len(self.best_moves) < self.k:
                self.best_moves.append((evaluation, moves))
            else:
                if self.depth % 2 == 0:
                    self.best_moves.append((evaluation, moves))
                    self.best_moves.remove(min(self.best_moves, key=lambda x: x[0]))
                else:
                    self.best_moves.append((evaluation, moves))
                    self.best_moves.remove(max(self.best_moves, key=lambda x: x[0]))
            return evaluation
        if turn:
            max_eval = -100000
            neighbours = random.sample(list(state.legal_moves), len(list(state.legal_moves)))
            for neighbour in neighbours:
                state.push(neighbour)
                evaluation = self.minimaxBestK(state, moves + [neighbour], depth - 1, alpha, beta, not turn)
                state.pop()
                max_eval = max(max_eval, evaluation)
                alpha = max(alpha, max_eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = 100000
            neighbours = random.sample(list(state.legal_moves), len(list(state.legal_moves)))
            for neighbour in neighbours:
                state.push(neighbour)
                evaluation = self.minimaxBestK(state, moves + [neighbour], depth - 1, alpha, beta, not turn)
                state.pop()
                min_eval = min(min_eval, evaluation)
                beta = min(beta, min_eval)
                if beta <= alpha:
                    break
            return min_eval
