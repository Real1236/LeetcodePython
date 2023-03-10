#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = []
        items = path.split("/")
        for item in items:
            if item == "..":
                directories.pop() if directories else ""
            elif item != "." and item != "":
                directories.append(item)
        return "/" + "/".join(directories)
    
# @lc code=end
solution = Solution()
print(solution.simplifyPath("/.hidden"))
