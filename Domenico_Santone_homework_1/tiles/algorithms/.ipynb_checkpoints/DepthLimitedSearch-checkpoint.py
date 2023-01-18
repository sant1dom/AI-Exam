from .AbstractSearchAlgorithm import AbstractSearchAlgorithm


class DepthLimitedSearch(AbstractSearchAlgorithm):
    def __init__(self, start_state, goal_state, depth):
        super().__init__(start_state, goal_state)
        self.depth = depth
        self.current_depth = 0

    def pick(self, horizon):
        if self.current_depth < self.depth:
            self.current_depth += 1
            return horizon.pop()
