from .AbstractSearchAlgorithm import AbstractSearchAlgorithm


class BFSearch(AbstractSearchAlgorithm):
    def pick(self):
        return self.horizon.pop(0)