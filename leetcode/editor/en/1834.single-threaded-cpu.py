#
# @lc app=leetcode id=1834 lang=python3
#
# [1834] Single-Threaded CPU
#

# @lc code=start
from collections import deque
import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = deque(sorted([(task[0], task[1], i) for i, task in enumerate(tasks)]))
        task_index = 0
        res = []
        heap = []
        time = 1

        while len(res) < len(tasks):
            while task_index < len(tasks) and tasks[task_index][0] <= time:
                heapq.heappush(heap, (tasks[task_index][1], tasks[task_index][2]))
                task_index += 1
            if heap:
                task = heapq.heappop(heap)
                time += task[0]
                res.append(task[1])
            else:
                time += 1

        return res
            
        
# @lc code=end
solution = Solution()

tasks = [[1,2],[2,4],[3,2],[4,1]]
print(solution.getOrder(tasks))

tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
print(solution.getOrder(tasks))
