# Question 3 - Sliding Window
# Given a binary array nums[] and an integer k, find the count of non-empty subarrays with a sum equal to k.

# Example 1:

# Input:
# nums = [1, 0, 1, 1, 0, 1]
# k = 2
# Output:
# 6
# Explanation:
# All valid subarrays are:  [1, 0, 1], [0, 1, 1], [1, 1], [1, 0, 1], [0, 1, 1, 0], [1, 1, 0].

# Example 2:

# Input:
# nums = [0, 0, 0, 0, 0]
# k = 0
# Output:
# 15
# Explanation:
# All subarrays have a sum equal to 0, and there are a total of 15 subarrays.

from typing import List


def count_subarrays_equal_k(nums: List[int], k: int) -> int:
    def count_subarrays_atmost_k(k: int) -> int:
        count = total = left = 0
        for right in range(len(nums)):
            total += nums[right]
            while left <= right and total > k:
                total -= nums[left]
                left += 1
            count += right - left + 1
        return count

    return count_subarrays_atmost_k(k) - count_subarrays_atmost_k(k - 1)

nums = [1, 0, 1, 1, 0, 1]
k = 2
print(count_subarrays_equal_k(nums, k))

nums = [0, 0, 0, 0, 0]
k = 0
print(count_subarrays_equal_k(nums, k))

nums = [1, 0, 1, 0, 1]
k = 2
print(count_subarrays_equal_k(nums, k))

nums = [1, 1, 1, 1, 1]
k = 3
print(count_subarrays_equal_k(nums, k))

# The implementation utilizes a sliding window approach to calculate the number of subarrays with sums at most k and at most k-1, then subtracts the latter from the former to isolate subarrays whose sum exactly equals k. The time complexity of this approach is O(N) as it involves a single pass through the array, and the space complexity is O(1).