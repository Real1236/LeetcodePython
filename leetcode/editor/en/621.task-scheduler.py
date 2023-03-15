#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from collections import Counter, deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        letters = Counter(tasks)
        heap = [-count for count in letters.values()]
        heapq.heapify(heap)

        time = 0
        queue = deque()
        while heap or queue:
            time += 1
            if heap:
                count = heapq.heappop(heap) + 1
                if count:
                    queue.append((count, time + n))
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        return time

# @lc code=end
solution = Solution()
print(solution.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
