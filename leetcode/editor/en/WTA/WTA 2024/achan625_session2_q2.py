# Question 2 - Arrays
# Given an unsorted array of integers, sort the array into a wave array. An array nums[0..n-1] is sorted in wave form if:
# nums[0] >= nums[1] <= nums[2] >= nums[3] <= nums[4] >= ...

# Example 1: 
# Input: nums = [10, 5, 6, 3, 2, 20, 100, 80]
# Output: [10, 5, 6, 2, 20, 3, 100, 80]
# Explanation: Here you can see the first element is larger than the second and the same thing is repeated again and again. It can be small element - larger element - small element too, all you need to maintain is the up-down fashion which represents a wave. There can be multiple answers.

# Example 2: 
# Input: nums = [20, 10, 8, 6, 4, 2]
# Output: [20, 8, 10, 4, 6, 2]
# Explanation: 20 > 8 < 10 > 4 < 6 > 2

from typing import List


def sortInWave(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(0, n, 2):
        if i > 0 and nums[i] < nums[i-1]:
            nums[i], nums[i-1] = nums[i-1], nums[i]
        
        if i < n-1 and nums[i] < nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
    
    return nums

nums1 = [10, 5, 6, 3, 2, 20, 100, 80]
print(sortInWave(nums1))

nums2 = [20, 10, 8, 6, 4, 2]
print(sortInWave(nums2))

nums3 = [0, 1, 2, 4, 5, 6]
print(sortInWave(nums3))

nums4 = [10]
print(sortInWave(nums4))