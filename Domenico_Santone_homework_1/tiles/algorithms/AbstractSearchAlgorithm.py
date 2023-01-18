from abc import ABC, abstractmethod
import time


class AbstractSearchAlgorithm(ABC):
    def __init__(self, start_state, goal_state):
        self.startState = start_state
        self.goalState = goal_state
        self.horizon = []
        self.explored = []

    def search(self):
        self.horizon.append(self.startState)
        while self.horizon:
            state = self.pick()
            if state == self.goalState:
                return self.backpath(state)
            self.explored.append(state)
            self.horizon.extend([s for s in state.neighbours() if s not in self.explored and s not in self.horizon])
        return False

    @abstractmethod
    def pick(self):
        pass

    def backpath(self, state):
        """
        This method returns the backpath from the goal state to the start state.
        :param state:
        :return:
        """
        path = []
        while state:
            path.append(state)
            state = state.parent
        path.reverse()
        return path

