#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        answers = [1] * (n + 1)
        for i in range(2, n + 1):
            total = 0
            for j in range(1, i + 1):
                left = j - 1
                right = i - j
                total += answers[left] * answers[right]
            answers[i] = total
        return answers[n]
        
# @lc code=end

# 1 : 1
# 2 : 2     1   
# 3 : 5     3  
# 4 : 14    9   
# 5 : 42    28
solution = Solution()
# print(solution.numTrees(1))
# print(solution.numTrees(2))
print(solution.numTrees(3))
print(solution.numTrees(4))
print(solution.numTrees(5))
print(solution.numTrees(6))
print(solution.numTrees(7))
print(solution.numTrees(8))