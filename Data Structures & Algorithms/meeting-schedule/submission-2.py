"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
requirements:
- array of tuples, each tuple contains start and end time.
- return boolean depending on whether condition is met

constraints:
- in a tuple, the start is always gauranteed to be less than end time
- conflict: does the start time <= the end time of another.
- array might not already be sorted so need to sort the array to make it easier to expect the future
    - do we need tie breakers?
=> sorting allows for O(n log n) to get O(n) during comparison/evaluations whereas if we did in line it would be O(n^2) at least

edge case: empty interval which means return true?
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        last_processed = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i].start < last_processed.end: # current starts before last processed ends
                return False
            # no conflict, then update last_processed
            last_processed = intervals[i]
        return True