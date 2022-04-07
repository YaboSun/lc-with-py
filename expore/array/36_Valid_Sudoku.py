"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        问题拆解：分为三个部分，第一部分判断行是否满足
        第二部分判断列是否满足
        第三部分判断3*3square是否满足
        :param board: 传入的数独板
        :return: true or false
        """
        return self.is_row_valid(board) and self.is_column_valid(board) and self.is_square_valid(board)

    def is_row_valid(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    def is_column_valid(self, board: List[List[str]]) -> bool:
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False

        return True

    def is_square_valid(self, board: List[List[str]]) -> bool:
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True

    def is_unit_valid(self, unit) -> bool:
        unit = [i for i in unit if i != "."]
        return len(set(unit)) == len(unit)