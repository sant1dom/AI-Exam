import numpy as np


class Board:
    def __init__(self, size, board=None, is_goal_state=False):
        """
        This class represents a board of a game. The board should be a square matrix, with values in the range [0, size - 1].
        :param size: The size of the board.
        """
        self._size = size
        # The board is represented as a numpy array containing the values of the tiles with no duplicates and the empty tile is represented as 0.
        if board is None:
            self._board = np.reshape(np.arange(size * size), (size, size))
            np.random.shuffle(self._board)
            self._board = np.transpose(self._board)
            np.random.shuffle(self._board)
        else:
            self._board = board
        # The parent of the current board for the backpath.
        self.parent = None

        # The cost of the current board.
        self.cost = 1
        # The goal state of the board.
        if not is_goal_state:
            self._goal_state = Board(size, np.reshape(np.arange(size * size), (size, size)), True)

    def get_goal_state(self):
        return self._goal_state

    def get_board(self):
        return self._board

    def __str__(self):
        out = ""
        for i in range(self._size):
            for j in range(self._size):
                out += str(self._board[i][j]) + "\t"
            out += "\n"
        return out

    def __repr__(self):
        return self.__str__()

    def get_size(self):
        return self._size

    def neighbours(self):
        """
        Returns the neighbours of the current board.
        :return: A list of the neighbours of the current board.
        """
        neighbours = []
        empty_tile = self._find_empty_tile()
        if empty_tile[0] > 0:
            state = self._swap_tiles(empty_tile, (empty_tile[0] - 1, empty_tile[1]))
            state.parent = self
            neighbours.append(state)
        if empty_tile[0] < self._size - 1:
            state = self._swap_tiles(empty_tile, (empty_tile[0] + 1, empty_tile[1]))
            state.parent = self
            neighbours.append(state)
        if empty_tile[1] > 0:
            state = self._swap_tiles(empty_tile, (empty_tile[0], empty_tile[1] - 1))
            state.parent = self
            neighbours.append(state)
        if empty_tile[1] < self._size - 1:
            state = self._swap_tiles(empty_tile, (empty_tile[0], empty_tile[1] + 1))
            state.parent = self
            neighbours.append(state)
        return neighbours

    def _find_empty_tile(self):
        """
        Finds the empty tile in the board.
        :return: The coordinates of the empty tile.
        """
        for i in range(self._size):
            for j in range(self._size):
                if self._board[i][j] == 0:
                    return i, j

    def _swap_tiles(self, empty_tile, param):
        """
        Swaps the empty tile with the tile at the given coordinates.
        :param empty_tile: The coordinates of the empty tile.
        :param param: The coordinates of the tile to swap with the empty tile.
        :return: A new board with the tiles swapped.
        """
        new_board = Board(self._size)
        new_board._board = np.copy(self._board)
        new_board._board[empty_tile[0]][empty_tile[1]] = self._board[param[0]][param[1]]
        new_board._board[param[0]][param[1]] = 0
        return new_board

    def __eq__(self, other):
        return np.array_equal(self._board, other.get_board())

    def __hash__(self):
        return hash(self._board.tostring())

    def __getitem__(self, item):
        return self._board[item]

    def getInvCount(self, arr):
        inv_count = 0
        empty_value = 0
        for i in range(0, 9):
            for j in range(i + 1, 9):
                if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                    inv_count += 1
        return inv_count

    # This function returns true if given
    # instance of puzzle is solvable
    def is_solvable(self):
        if self._size != 3:
            return true
        # Count inversions in given 8 puzzle
        inv_count = self.getInvCount([j for sub in self._board for j in sub])

        # return true if inversion count is even.
        return inv_count % 2 == 0
