"""
requirements:
- lowest number of intervals to REMOVE (different from merging/combining) to make it non-overlapping 
- at least 1 interval in it. 

constraints:
- common point is non-overlapping so < and >
    => a current interval is overlapping with another interval if curr's start < end and curr's start >= start OR curr's end > start and <= end. 
- brute force: remove an interval everytime it overlaps with another interval which would be O(n^2) since you are comparing each interval with every other interval and then removing the interval with most overlaps till there's no overlaps. 


- optimization: ideally, you want to remove the interval that causes the most overlaps with other intervals like if one interval groups/overlaps with 3 intervals, removing that ONE interval would solve the biggest problem (regardless of whether the rest of those 3 overlap too)

- need to iterate through the interval so at least O(n) time, but should sort by start time to make comparions efficiently so O(n log n)


constraint is the comparisons you have to do. anything we can know greedily? => does sorting make it like not greedy?

"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        min_count = 0
        intervals.sort(key=lambda x:x[1])
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                min_count += 1
            else:
                prev_end = intervals[i][1]





        return min_count