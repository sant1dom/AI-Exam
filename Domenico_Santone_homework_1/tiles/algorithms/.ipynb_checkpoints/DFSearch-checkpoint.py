from .AbstractSearchAlgorithm import AbstractSearchAlgorithm


class DFSearch(AbstractSearchAlgorithm):
    def pick(self, horizon):
        return horizon.pop()
