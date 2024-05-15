from collections import defaultdict
class TimeMap:
    
    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ts_list = self.map[key] # sort (timestamps, val) into a list
        if not ts_list: return ""
        l = 0
        r = len(ts_list)-1
        if timestamp >= ts_list[r][0]:
            return ts_list[r][1]
        if timestamp < ts_list[l][0]:
            return "" 
        while l<=r:
            m = (l+r)//2
            if ts_list[m][0] == timestamp:
                return ts_list[m][1]
            if ts_list[m][0] > timestamp: #left
                r = m-1
            else:
                l = m+1
        return ts_list[l-1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)