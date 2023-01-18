from .AbstractSearchAlgorithm import AbstractSearchAlgorithm


class BestFirstSearch(AbstractSearchAlgorithm):
    def __init__(self, start_state, goal_state, heuristic):
        super().__init__(start_state, goal_state)
        self.heuristic = heuristic

    def pick(self):
        el = min(self.horizon, key=lambda x: self.heuristic(x))
        self.horizon.remove(el)
        return el
