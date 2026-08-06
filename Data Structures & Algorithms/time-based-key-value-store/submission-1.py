"""
- key-value means data structure should be a hash map or dict
=> key = key, value = [] and then append timestamp to it? 
=> each value in [] could be a tupl storing (value, timestamp)

- for get(), we want to return highest timestamp that is closest to timestamp in get() parameter. if there are no values, return ""
=> we will need to binary search through that list. 
- how do you frame that binary search problem?
=> want to find the maximum value is less than or equal to timestamp
=> WE ARE GIVEN THAT "ALL TIMESTAMPS of set are strictly increasing so you can assume timestamps will be added to dict in inc. order
=> if mid is less than or equal, save it as possible answer move left to mid + 1
=> if mid is greater than timestamp, move right pointer to mid - 1 since all values to the right also too big for timestamp
=> stop once right < left


edge case:
- can you add multiple timestamp values that are same in the array like duplicates? -> no according to problem
- trying to get from a key that isn't in the hash map
"""
class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # edge case
        if key not in self.hashmap:
            return ""

        l = 0
        array = self.hashmap[key]
        print(array)
        r = len(array) - 1
        ans = ""
        while l <= r:
            mid = l + (r - l) // 2
            print(mid)
            print(array[mid])
            if array[mid][1] <= timestamp:
                l = mid + 1
                ans = array[mid][0]
            elif array[mid][1] > timestamp:
                r = mid - 1
            
        return ans