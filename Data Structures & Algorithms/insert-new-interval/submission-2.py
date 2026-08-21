"""
requirements:
- starting array has NON-OVERLAPPING intervals
- need to return the FINAL INTERVAL so ideally we need to edit in place. not pushing/popping or creating a new interval. 


constraints:
- array is already sorted, ascending start times
- need to place new Interval into the array where its still sorted and there's no overlaps i.e no end goes into the inserted start,end range and no other intervals start in inserted start,end range
- overlapping means if <= or >=, i.e 2 and 2.2 are overlapping
- can merge intervals i.e take the min start time and max end time between 2 intervals

- where should the newInterval be placed? -> when it has a greater start time than previous interval but less start time than next interval.

***how do you tell when there needs to be a merge?***
=> no merge if newIntervals start is > curr interval's end or < than curr_interval's start => i.e put the newInterval before that curr_interval. or put that newInterval AFTER curr_interval.
- need merge if start is within range or end is within range, or BOTH, then take min of starts and max of ends and append it the array, 


NOTICE HOW: for an newInterval to not conflict, its values have to be both the maxes or both the mins compared to another interval.

wait: on merge, just update newInterval. and only append newInterval when there's no conflicts, this could be after a bunch of merges or not. 



edge cases:
- if intervals is [], just return the newInterval]
- an interval has one or multiple ends into its range 
- AND/OR an intervla has one or multiple starts into range. 
- don't append a new interval until its completely less than curr interval start. -> just because its after curr interval's end, doesn't mean it holds that condition for both. 
=> if it never ends before, then we add it at the end REGARDLESS of whether ans contains elements i.e has valid elements or if it was just empty
- 

- given that originally intervals is non-overlapping, newInterval could cause multiple to be merged if its range is big enough. 
- what happens after newInterval merges with another interval because of overlap, but then that new interval conflicts with another. 

solution insight: 
- just create a new interval and add, pop, and merge as needed. since if you need to merge, it will only mean popping the most recent and updating it. and then keep on adding till all of its done. 


"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ans = []
        is_added = False
        for i in range(len(intervals)):
            # newInterval starts and ends before curr interval start
            if not is_added and newInterval[0] < intervals[i][0] and newInterval[1] < intervals[i][0]:
                is_added = True
                ans.append(newInterval)
                ans.extend(intervals[i:])
            # newInterval starts and ends after curr intervals' end
            elif newInterval[0] > intervals[i][1] and newInterval[1] > intervals[i][1]:
                ans.append(intervals[i])
            # merge is necessary:
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        if not is_added:
            ans.append(newInterval)
        return ans
        