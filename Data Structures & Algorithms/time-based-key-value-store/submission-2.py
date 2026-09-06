class TimeMap:

    def __init__(self):
        self.container = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.container:
            self.container[key] = []
        self.container[key].append((timestamp,value))

        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.container:
            return ""
        n = len(self.container[key])
        left=0
        right= n-1
        

        while right>=left:
            
            mid = left+(right-left)//2
            

            if self.container[key][mid][0] == timestamp:
                return self.container[key][mid][1]
            elif self.container[key][mid][0] < timestamp:
                left = mid+1
            else:
                right = mid-1
        
        if right >= 0:
            return self.container[key][right][1]
        
        return ""





