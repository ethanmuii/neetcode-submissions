"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
requirements: same as Meeting Room I problem

constraints:
- 2 intervals where end of previous and start of later are the same are NOT considered overlap, so only use > or <
- finding the MIN number of rooms, when is a room needed?
=> only when there's a conflict cuz then that later conflicting intervals needs to be put in a different space so every conflict means increase room by 1. 
- you need at least 1 room though regardless of interval count?

*** as the room count goes up, you only need to track the MIN end time between all intervals currently in room. since  that's the room that will open up first***
ex. [(0,6),(5,10),(9,20)], if you look at the last interval processed, then you will think you need 3 rooms, but you only need 2. => need to keep track of the min end time of all the rooms being occupied. can do that greedily by checking every comparison and taking the global min between them
=> do you have to check every time or only on comparison?
=> only need to do that on comparison because once an interval's start time is later than that min end time, the min_end time needs to get reset or else it will always stay the same


edge case:
- empty intervals, return 0?
- 1 interval, only need 1 room
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        # need to print
        for interval in intervals:
            print(interval.start, interval.end)




        min_queue = []
        heapq.heappush(min_queue, intervals[0].end)
        for i in range(1, len(intervals)):
            later_start = intervals[i].start
            if later_start >= min_queue[0]:
                heapq.heappop(min_queue)
            heapq.heappush(min_queue, intervals[i].end)
        return len(min_queue)

"""
room 1: (25, 579) room 2: (218, 918) min_end = 579
room 1: (623, 1320) room 2: (218, 918) min_end = 918
room 1: (623, 1320) room 2: (218, 918) room 3: (685, 1353) min_end 918
room 1: (623 1320) room 2: (1281, 1307) room 3: (685, 1353) min_end 1307
*** here's where i went wrong, it made min_end the last previous which is 1353 which  is not the min when it should be 1307, it should be the min between all the active rooms instead. 

-> how do you do this time efficiently?
- how should you track all the rooms? and how should pop efficiently? priority queue? 
"""
        