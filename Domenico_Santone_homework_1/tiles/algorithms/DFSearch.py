from .AbstractSearchAlgorithm import AbstractSearchAlgorithm


class DFSearch(AbstractSearchAlgorithm):
    def pick(self):
        return self.horizon.pop()
