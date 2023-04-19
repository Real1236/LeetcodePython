#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(ip: str, num: int, index: int) -> None:
            for i in range(1, 4):
                if num == 5 or index + i > len(s):
                    return
                cur = s[index : index + i]
                if len(cur) > 1 and cur[0] == "0":
                    return
                if int(cur) >= 0 and int(cur) <= 255:
                    if num == 4 and index + i == len(s):
                        ip += cur
                        res.append(ip)
                        return
                    ip += cur + "."
                    backtrack(ip, num + 1, index + i)
                    ip = ip[:len(ip) - len(cur) - 1]
        
        backtrack("", 1, 0)
        return res
        
# @lc code=end
solution = Solution()
print(solution.restoreIpAddresses("25525511135"))
print(solution.restoreIpAddresses("101023"))
