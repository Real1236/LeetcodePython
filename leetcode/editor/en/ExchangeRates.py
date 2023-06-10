from collections import defaultdict

input = ["USD,CAD,1.3;USD,GBP,0.71;USD,JPY,109;GBP,JPY,155","USD","JPY"]

adjList = defaultdict(list)
selectedTarget = []

for line in input:
    if len(line) > 5:
        rates = line.split(";")
        for rate in rates:
            c1, c2, exchange = rate.split(",")
            adjList[c1].append((c2, float(exchange)))
            adjList[c2].append((c1, 1/float(exchange)))
    else:
        selectedTarget.append(line[:3])
    
selected, target = selectedTarget[0], selectedTarget[1]
visited = set()
def dfs(cur: str, value: float) -> float:
    if cur in visited:
        return 0
    if cur == target:
        return value
    visited.add(cur)
    maxValue = 0
    for country, rate in adjList[cur]:
        maxValue = max(maxValue, dfs(country, value * rate))
    visited.remove(cur)
    return maxValue

res = dfs(selected, 1)
if res > 0:
    print(res)
else:
    print(-1.0)