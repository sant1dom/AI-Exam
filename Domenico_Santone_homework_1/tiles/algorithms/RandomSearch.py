from random import randint
from .AbstractSearchAlgorithm import AbstractSearchAlgorithm


class RandomSearch(AbstractSearchAlgorithm):
    def pick(self):
        return self.horizon.pop(randint(0, len(self.horizon)-1))