class TimeMap:
    # { key : [timestamp, value] }



    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # check if key in map yet
        if key not in self.keyStore:
            self.keyStore[key] = []
        # append value timestamp pair
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.keyStore.get(key, [])

        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r)// 2
            # closest we got
            if values[m][1] <= timestamp:
                result = values[m][0]
                l = m + 1
            else: 
                r = m - 1
        return result
        
