def simple(self, state, goalState):
    return 0

def differences(self, state, goal_state):
    diffs = 0
    for i in range(state.get_size()):
        for j in range(state.get_size()):
            if state[i][j] != goal_state[i][j]:
                diffs += 1
    return diffs

def manhattanDistance(self, state, goal_state):
    result = 0
    for i in range(0, state.get_size()):
        for j in range(0, state.get_size()):
            index = state.get_board()[i][j] - 1
            distance = (2 - i) + (2 - j) if index == -1 else abs(i - (index / state.get_size())) + abs(
                j - (index % state.get_size()))
            result += distance
    return result

def calculateManhattan(initial_state):
    initial_config = [j for i in initial_state for j in i]
    manDict = 0
    for i,item in enumerate(initial_config):
        prev_row,prev_col = int(i/ initial_state.get_size()) , i % initial_state.get_size()
        goal_row,goal_col = int(item /initial_state.get_size()),item % initial_state.get_size()
        manDict += abs(prev_row-goal_row) + abs(prev_col - goal_col)
    return manDict
