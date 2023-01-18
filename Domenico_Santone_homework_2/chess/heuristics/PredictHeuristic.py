from typing import Any

from .AbstractHeuristic import AbstractHeuristic
import pickle
import chess
import numpy as np
import warnings

class PredictHeuristic(AbstractHeuristic):
    def __init__(self):
        super().__init__()
        self.regression = None
        warnings.filterwarnings("ignore")


    def load_model(self):
        if self.regression is None:
            with open('hist.sav', 'rb') as f:
                self.regression = pickle.load(f)

    def board_to_array(self, board):
        # This function converts a board to a numpy array
        # The array is 1x64
        lista = []
        for i in range(64):
            if board.piece_at(i) is None:
                lista.append(0)
            else:
                lista.append(board.piece_at(i).piece_type if board.piece_at(i).color else -board.piece_at(i).piece_type)
        return np.array(lista)

    def evaluate(self, state: chess.Board):
        self.load_model()
        nparray = self.board_to_array(state)
        prediction = self.regression.predict(nparray.reshape(1, -1))[0]
        return prediction

