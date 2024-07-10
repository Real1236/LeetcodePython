# Question 1
# Given an array of digits, form two numbers using digits in the array which have the minimum possible sum.

# All digits must be used once, and only once.

# Example 1:
# Input: [6, 8, 4, 5, 2, 3]
# Output: 604

# Explanation: The minimum sum of 604 is formed by numbers 358 and 246.

# Example 2:
# Input: [5, 2, 0, 1, 7]
# Output: 42

# Explanation: The minimum sum of 42 is formed by numbers 15 and 027   

from typing import List


def min_sum(nums: List[int]) -> int:
    nums.sort()
    num1, num2 = 0, 0
    for i, n in enumerate(nums):
        if i % 2:
            num2 = 10 * num2 + n
        else:
            num1 =10 * num1 + n
    return num1 + num2

print(min_sum([6, 8, 4, 5, 2, 3]))
print(min_sum([5, 2, 0, 1, 7]))
print(min_sum([1, 3, 9, 7, 8]))
print(min_sum([0, 1, 2, 3, 4, 5]))

# The minimum sum occurs by summing the two smallest numbers possible, which is found by putting the smaller digits first. Therefore, the algorithm sorts the nums and iterates through the sorted list, assigning even-indexed elements to one number and odd-indexed elements to another, effectively minimizing the sum of these two constructed numbers. The time complexity of this solution is O(nlogn) due to the sorting step. The space complexity is O(1)