#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
from collections import deque


class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.data.get(key, [])
        left, right = 0, len(values) - 1
        res = ""
        while left <= right:
            middle = (left + right) // 2
            if values[middle][1] <= timestamp:
                res = values[middle][0]
                left = middle + 1
            else:
                right = middle - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

