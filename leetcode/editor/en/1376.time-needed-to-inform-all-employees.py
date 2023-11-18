class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        manToEmp = defaultdict(list)
        for e, m in enumerate(manager):
            manToEmp[m].append(e)

        def dfs(curE: int, curM: int) -> int:
            employees = manToEmp[curE]
            time = 0
            for e in employees:
                time = max(time, dfs(e, curE))
            time += informTime[curM] if curM != -1 else 0
            return time
        
        return dfs(headID, -1)
