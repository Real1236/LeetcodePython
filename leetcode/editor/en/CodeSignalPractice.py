class HashMap:
    def __init__(self):
        self.map = {}
        self.key_offset = 0
        self.value_offset = 0

    def insert(self, x, y):
        self.map[x - self.key_offset] = y - self.value_offset

    def get(self, x):
        return self.map.get(x - self.key_offset, None) + self.value_offset

    def addToKey(self, x):
        self.key_offset += x

    def addToValue(self, y):
        self.value_offset += y

def solution(queryType, query):
    map = HashMap()
    result = 0
    for i in range(len(queryType)):
        if queryType[i] == "insert":
            map.insert(query[i][0], query[i][1])
        elif queryType[i] == "get":
            result += map.get(query[i][0])
        elif queryType[i] == "addToKey":
            map.addToKey(query[i][0])
        elif queryType[i] == "addToValue":
            map.addToValue(query[i][0])
    return result

queryType = ["insert", 
 "insert", 
 "addToKey", 
 "addToKey", 
 "addToKey", 
 "insert", 
 "addToValue", 
 "addToKey", 
 "addToKey", 
 "get"]
query = [[-5,-2], 
 [2,4], 
 [-1], 
 [-3], 
 [1], 
 [3,-2], 
 [-4], 
 [-2], 
 [2], 
 [-8]]
print(solution(queryType, query))