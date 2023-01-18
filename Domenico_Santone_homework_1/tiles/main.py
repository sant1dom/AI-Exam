from algorithms.DFSearch import DFSearch
from algorithms.BFSearch import BFSearch
from algorithms.RandomSearch import RandomSearch
from algorithms.BestFirstSearch import BestFirstSearch
from algorithms.AStarSearch import AStarSearch
from heuristics.Heuristics import calculateManhattan
from heuristics.Heuristics import differences

import time
from representation.Board import Board

if __name__ == '__main__':
    board = Board(4)
    while not board.is_solvable():
        board = Board(4)
    print("Board:", board, sep="\n")
    if board.is_solvable():
        print("Solvable")
        print("Starting search...")
        solver = AStarSearch(board, board.get_goal_state(), calculateManhattan)
        solver2 = BestFirstSearch(board, board.get_goal_state(), calculateManhattan)
        start = time.time()
        solution = solver.search()
        end = time.time()
        print("A* search took", end - start, "seconds")
        print("Solution:", solution, sep="\n")
        start = time.time()
        solution = solver2.search()
        end = time.time()
        print("Best first search took", end - start, "seconds")
        print("Solution:", solution, sep="\n")

    else:
        print("Unsolvable")
