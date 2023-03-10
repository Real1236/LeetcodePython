# There are n dominoes in a line, and we place each domino vertically upright. 
# In the beginning, we simultaneously push some of the dominoes either to the left 
# or to the right. 
# 
#  After each second, each domino that is falling to the left pushes the 
# adjacent domino on the left. Similarly, the dominoes falling to the right push their 
# adjacent dominoes standing on the right. 
# 
#  When a vertical domino has dominoes falling on it from both sides, it stays 
# still due to the balance of the forces. 
# 
#  For the purposes of this question, we will consider that a falling domino 
# expends no additional force to a falling or already fallen domino. 
# 
#  You are given a string dominoes representing the initial state where: 
# 
#  
#  dominoes[i] = 'L', if the iᵗʰ domino has been pushed to the left, 
#  dominoes[i] = 'R', if the iᵗʰ domino has been pushed to the right, and 
#  dominoes[i] = '.', if the iᵗʰ domino has not been pushed. 
#  
# 
#  Return a string representing the final state. 
# 
#  
#  Example 1: 
# 
#  
# Input: dominoes = "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second 
# domino.
#  
# 
#  Example 2: 
#  
#  
# Input: dominoes = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
#  
# 
#  
#  Constraints: 
# 
#  
#  n == dominoes.length 
#  1 <= n <= 10⁵ 
#  dominoes[i] is either 'L', 'R', or '.'. 
#  
# 
#  Related Topics Two Pointers String Dynamic Programming 👍 3050 👎 183
from collections import deque


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        queue = deque()

        for index, direction in enumerate(dom):
            if direction != ".":
                queue.append((index, direction))

        while queue:
            index, direction = queue.popleft()

            if direction == "L":
                if index > 0 and dom[index - 1] == ".":
                    dom[index - 1] = "L"
                    queue.append((index - 1, "L"))
            else:
                if index < len(dom) - 1 and dom[index + 1] == ".":
                    if index < len(dom) - 2 and dom[index + 2] == "L":
                        queue.popleft()
                    else:
                        dom[index + 1] = "R"
                        queue.append((index + 1, "R"))

        return "".join(dom)


# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
solution.pushDominoes(".L.R...LR..L..")
#                      0         1         2         3         4         5         6         7         8         9
#                      0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
# solution.pushDominoes("...RL....R.L.L........RR......L....R.L.....R.L..RL....R....R......R.......................LR.R..L.R.")
#                     "...RL....R.LLL........RRRRRLLLL....R.L.....R.L..RL....RRRRRRRRRRRRRRRRRRRRRLLLLLLLLLLLLLLLLRRRRLL.RR"
#                     "...RL....R.LLL........RRRRRLLLL....R.L.....R.L..RL....RRRRRRRRRRRRRRRRRRRRRRRR.LLLLLLLLLLLLRRRRLL.RR"
