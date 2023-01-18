import numpy as np

def simple(self, state, goalState):
    return 0


def differences(self, state, goal_state):
    diffs = 0
    for i in range(state.get_size()):
        for j in range(state.get_size()):
            if state[i][j] != goal_state[i][j]:
                diffs += 1
    return diffs


def calculateManhattan(initial_state):
    initial_config: np.ndarray = np.concatenate(initial_state.get_board())
    manDict = 0
    for i, item in enumerate(initial_config):
        prev_row, prev_col = int(i / initial_state.get_size()), i % initial_state.get_size()
        goal_row, goal_col = int(item / initial_state.get_size()), item % initial_state.get_size()
        manDict += abs(prev_row - goal_row) + abs(prev_col - goal_col)
    return manDict
