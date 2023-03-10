#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            numsA, numsB = nums1, nums2
        else:
            numsA, numsB = nums2, nums1
        
        total = len(numsA) + len(numsB)
        half = total // 2
        left, right = 0, len(numsA) - 1
        while True:
            partA = left + (right - left) // 2
            partB = half - partA - 2

            leftA = numsA[partA] if partA >= 0 else float("-infinity")
            rightA = numsA[partA + 1] if partA < len(numsA) - 1 else float("infinity")
            leftB = numsB[partB] if partB >= 0 else float("-infinity")
            rightB = numsB[partB + 1] if partB < len(numsB) - 1 else float("infinity")

            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                else:
                    return min(rightA, rightB)
            elif leftA > rightB:
                right = partA - 1
            else:
                left = partA + 1
        
# @lc code=end
solution = Solution()
print(solution.findMedianSortedArrays([1,3], [2]))
print(solution.findMedianSortedArrays([1,2], [3,4]))
print(solution.findMedianSortedArrays([], [1]))
