class TimeMap:

    def __init__(self):
        self.timeMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        vals = self.timeMap.get(key, dict())
        vals[timestamp] = value
        self.timeMap[key] = vals


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        sortedKeys = list(self.timeMap[key].keys())
        currKey = None

        for k in sortedKeys:
            if k > timestamp:
                break
            currKey = k
        
        return self.timeMap[key][currKey] if currKey else ""
                
