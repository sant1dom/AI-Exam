from .AbstractSearchAlgorithm import AbstractSearchAlgorithm


class AStarSearch(AbstractSearchAlgorithm):
    def __init__(self, start_state, goal_state, heuristic):
        super().__init__(start_state, goal_state)
        self.heuristic = heuristic

    def pick(self, horizon):
        return min(horizon, key=lambda x: x.cost + self.heuristic(x, self.goalState))
