#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjList = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adjList[pattern].append(word)

        visited = set()
        q = deque([beginWord])
        res = 1
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if cur == endWord:
                    return res
                for i in range(len(cur)):
                    pattern = cur[:i] + "*" + cur[i + 1:]
                    for word in adjList[pattern]:
                        if word not in visited:
                            q.append(word)
                            visited.add(word)
            res += 1
        return 0
            
        
# @lc code=end
solution = Solution()
print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
