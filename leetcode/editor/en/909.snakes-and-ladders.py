#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        side_length = len(board)
        squares = deque([self.boustrophedon_coordinate(1, side_length)])
        count = 1
        visit = set()
        while squares:
            num_squares = len(squares)
            for i in range(num_squares):
                cur = squares.popleft()
                for i in range(1, 7):
                    next = self.boustrophedon_number(cur, side_length) + i
                    row, col = self.boustrophedon_coordinate(next, side_length)
                    if board[row][col] != -1:
                        row, col = self.boustrophedon_coordinate(board[row][col], side_length)
                    if self.boustrophedon_number((row, col), side_length) >= side_length ** 2:
                        return count
                    if (row,col) not in visit:
                        squares.append((row, col))
                        visit.add((row,col))
            count += 1
        return -1
                    
    def boustrophedon_coordinate(self, n: int, side_length: int) -> tuple:
        row = (n - 1) // side_length
        col = (n - 1) % side_length
        if row % 2 == 0:
            return (side_length - 1) - row, col
        return (side_length - 1) - row, (side_length - 1) - col
    
    def boustrophedon_number(self, coord: tuple, side_length: int) -> int:
        row = (side_length - 1) - coord[0]
        col = coord[1]
        if row % 2 == 0:
            return (row * side_length) + col + 1
        return (row * side_length) + (side_length - col)

        
# @lc code=end
solution = Solution()
# board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
board = [[1,1,-1],[1,1,1],[-1,1,1]]
print(solution.snakesAndLadders(board))