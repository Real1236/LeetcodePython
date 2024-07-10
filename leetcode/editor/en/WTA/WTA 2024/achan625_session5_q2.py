# Question 2
# You're going skiing on Mount Everest, and you have two options: Ski down the mountain to Tibet (exit top or left) or ski down the mountain to Nepal (exit bottom or right). 

# The mountain is an m x n matrix, where the value of each cell represents the altitude. You can ski from your current cell to an adjacent cell (up, down, left, right) that is less than or equal in altitude, but not higher. You may start on any cell and you may leave the matrix by going off the top, bottom, left, or right side.

# Return the number of cells you can start on and reach both Tibet and Nepal.

# Example:
# Input:
# everest = [  
#     [1, 2, 2, 3, 5],
#     [3, 2, 3, 4, 4],
#     [2, 4, 5, 3, 1],
#     [6, 7, 1, 4, 5],
#     [5, 1, 1, 2, 4]]

# Output: 7

# Explanation: You can reach both countries from the following cells: [[0,4], [1,3], [1,4], [2,2], [3,0], [3,1], [4,0]]

from collections import deque
from typing import List


def reachTibetAndNepal(everest: List[List[int]]) -> int:
    def bfs(queue: deque) -> set:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        while queue:
            row, col = queue.popleft()
            visited.add((row, col))
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if (new_row < 0 or new_col < 0
                    or new_row >= len(everest) or new_col >= len(everest[0])
                    or (new_row, new_col) in visited):
                    continue
                if everest[new_row][new_col] >= everest[row][col]:
                    queue.append((new_row, new_col))
        return visited

    
    queue = deque([])
    for row in range(len(everest)):
        queue.append((row, 0))
    for col in range(len(everest[0])):
        queue.append((0, col))

    tibet = bfs(queue)

    queue = deque([])
    for row in range(len(everest)):
        queue.append((row, len(everest[0]) - 1))
    for col in range(len(everest[0])):
        queue.append((len(everest) - 1, col))

    nepal = bfs(queue)
    
    return len(tibet.intersection(nepal))

everest = [  
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]]
print(reachTibetAndNepal(everest))

everest = [
    [5, 4, 3, 2, 1],
    [4, 3, 2, 1, 0],
    [3, 2, 1, 0, -1],
    [2, 1, 0, -1, -2],
    [1, 0, -1, -2, -3]]
print(reachTibetAndNepal(everest))

everest = [
    [1, 1, 1, 1, 1],
    [1, 2, 2, 2, 1],
    [1, 2, 3, 2, 1],
    [1, 2, 2, 2, 1],
    [1, 1, 1, 1, 1]]
print(reachTibetAndNepal(everest))

# Used BFS to find all the cells that can flow to Tibet and all the cells that can flow to Nepal. Took the intersection of the two sets since those are the cells that can flow to both. TC and SC is O(n) because of BFS.