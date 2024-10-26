#
# @lc app=leetcode id=2468 lang=python3
#
# [2468] Split Message Based on Limit
#

# @lc code=start
from typing import List


class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        def splitIntoParts(numParts: int) -> List[str]:
            res = []
            msgIndex = 0
            for page in range(1, numParts + 1):
                suffix = "<%d/%d>" % (page, numParts)
                msgLen = limit - len(suffix)
                nextMsgIndex = min(msgIndex + msgLen, len(message))
                msgPart = message[msgIndex : nextMsgIndex]
                msgIndex = nextMsgIndex
                res.append(msgPart + suffix)

                if nextMsgIndex == len(message) and page < numParts:
                    return ["lower"]
            
            if msgIndex < len(message):
                return ["higher"]
                
            return res
            
        if limit <= 5:
            return []
        res = None

        msgLen = len(message)
        digits = len(str(msgLen))
        for digit in range(1, digits + 1):
            low, high = max(1, 10 ** (digit - 1)), min(10 ** digit, len(message))
            while low <= high:
                numParts = (low + high) // 2
                splitMessage = splitIntoParts(numParts)
                if splitMessage == ["lower"]:
                    high = numParts - 1
                elif splitMessage == ["higher"]:
                    low = numParts + 1
                else:
                    low = numParts + 1
                    if not res or len(splitMessage) < len(res):
                        res = splitMessage

        return res if res else []

# @lc code=end
solution = Solution()

message = "this is really a very awesome message"
limit = 9
ans = ["thi<1/14>","s i<2/14>","s r<3/14>","eal<4/14>","ly <5/14>","a v<6/14>","ery<7/14>"," aw<8/14>","eso<9/14>","me<10/14>"," m<11/14>","es<12/14>","sa<13/14>","ge<14/14>"]
res = solution.splitMessage(message, limit)
print(res)
assert res == ans

message = "abbababbbaaa aabaa a"
limit = 8
ans = ["abb<1/7>","aba<2/7>","bbb<3/7>","aaa<4/7>"," aa<5/7>","baa<6/7>"," a<7/7>"]
res = solution.splitMessage(message, limit)
print(res)
assert res == ans