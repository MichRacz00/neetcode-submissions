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
        
        keys = list(self.timeMap[key].keys())
        keys.sort()
        currKey = None

        l, r = 0, len(keys) - 1
        while l <= r:
            m = (l + r) // 2
            if timestamp < keys[m]:
                r = m - 1
            else:
                if not currKey:
                    currKey = keys[m]
                else:
                    currKey = max(currKey, keys[m])
                l = m + 1
        
        return self.timeMap[key][currKey] if currKey else ""
                
