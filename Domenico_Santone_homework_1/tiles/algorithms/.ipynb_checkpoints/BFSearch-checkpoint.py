from .AbstractSearchAlgorithm import AbstractSearchAlgorithm


class BFSearch(AbstractSearchAlgorithm):
    def pick(self, horizon):
        return horizon.pop(0)