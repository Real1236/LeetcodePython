# Question 3
# You are given a matrix of size M * N, which contains some combination of the following values:
# 0: Empty
# 1: Fresh apple
# 2: Spoiled apple
# Every minute, a spoiled apple can ruin all fresh apples adjacent to it. Calculate the minimum time required for all apples to be spoiled. Return -1 if it is impossible for all apples to be spoiled.

# Example 1:
# Input: apples = [
#     [2, 1, 0, 2, 1], 
#     [1, 0, 1, 2, 1], 
#     [1, 0, 0, 2, 1]]
# Output: 2
# Explanation: It will take 2 minutes for all fresh apples to become spoiled.

# Example 2:
# Input: apples2 = [
#     [2, 1, 0, 2, 1], 
#     [0, 0, 1, 2, 1], 
#     [1, 0, 0, 2, 1]]
# Output: -1
# Explanation: The fresh apple in the bottom left of the array can never become spoiled.

from collections import deque
from typing import List


def spoil_time(apples: List[List[int]]) -> int:
    q = deque([])
    for row in range(len(apples)):
        for col in range(len(apples[0])):
            if apples[row][col] == 2:
                q.append((row, col))
    
    time = -1
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
        num_spoiled_apples = len(q)
        for _ in range(num_spoiled_apples):
            row, col = q.popleft()
            for dx, dy in dirs:
                new_row, new_col = row + dx, col + dy
                if new_row < 0 or new_col < 0 or new_row >= len(apples) or new_col >= len(apples[0]):
                    continue
                if apples[new_row][new_col] == 1:
                    q.append((new_row, new_col))
                    apples[new_row][new_col] = 2
        time += 1
    
    spoiled_apple_found = False
    for row in range(len(apples)):
        for col in range(len(apples[0])):
            if apples[row][col] == 1:
                return -1
            elif apples[row][col] == 2:
                spoiled_apple_found = True
    
    return time if spoiled_apple_found else 0

apples = [
    [2, 1, 0, 2, 1], 
    [1, 0, 1, 2, 1], 
    [1, 0, 0, 2, 1]
]
print(spoil_time(apples))

apples = [
    [2, 1, 0, 2, 1], 
    [0, 0, 1, 2, 1], 
    [1, 0, 0, 2, 1]
]
print(spoil_time(apples))

apples = [[0]]
print(spoil_time(apples))

apples = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(spoil_time(apples))

# Used BFS to keep track of the spoiled apples. Each BFS loop represents a unit of time. Check for edge cases for if it's impossible to spoil all apples or if there are no apples at all. TC is O(n) and SC is O(n)