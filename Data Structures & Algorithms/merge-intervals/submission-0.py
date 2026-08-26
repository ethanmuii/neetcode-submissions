"""
requirements:
- each index in intervals is a list of length 2
- return the list that has no overlapping intervals i.e combine intervals when overlapping, and then once it has no overlaps then we can add it. 

constraints:
- if start and end dates are equal, that is overlapping. same applies within any overlapping in ranges
- next interval is overlapping with previous if its start is >= start and <= start <= end. 

edge cases:
- do intervals array start in sorted order by start time?=> NO, so sort it first to make linear search easy
- do we only care about the next inerval's start? or should we compare about its end. => i think because its sorted we can only worry about the start and not the end. => this is because an interval isn't added until its next one is guaranteed to not have conflicts. i.e let's say an interval's END intersects with the next interval's start. this condition will get checked when that interval looks at its previous and sees it's start time <= end and must be greater than equal to start since start can't be greater than end 
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        # add the first interval to answer
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            prev = output[-1]
            if intervals[i][0] >= prev[0] and intervals[i][0] <= prev[1]:
                new_interval = [prev[0], max(prev[1], intervals[i][1])]
                output.pop()
                output.append(new_interval)
            else: # no overlapping with previous then we can append it
                output.append(intervals[i])
        return output

