#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters = Counter(s)
        prev = -1
        res = []
        partition = {}
        for i, c in enumerate(s):
            if c not in partition:
                partition[c] = letters[c]
            partition[c] -= 1
            if partition[c] == 0:
                partition.pop(c)
                if not partition:
                    res.append(i - prev)
                    prev = i
        return res

# @lc code=end
solution = Solution()
print(solution.partitionLabels("ababcbacadefegdehijhklij"))
