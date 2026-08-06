"""
in english: want the slowest eating rate where we can still eat all bananas within the time limit

can only eat from 1 pile per hour regardless of eating rate

cannot overeat the number of bananas.

since we can only eat from 1 pile per hour, the fastest we can eat the number of bananas is len(piles) where h must be at least that number

in order to succesfully eat 1 pile her hour, our eating rate needs to be the maximum number in piles or the biggest pile in piles[i]
=> because if its not, that pile will take 2 hours. remember we can "overeat" from a number of pile. i.e our eating rate is 25 and the pile only has 8 bananas, will still take 1 hour

- the max eating rate in the range is max(piles)
- min eating rate in the range must be 1. 0 not valid cuz ur not eating
- if you find a value that doesn't make it in time, need to speed up the eating rate
- if you find a value that does make it in time, can you slow down the eating rate even more
"""
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles) # maxRate
        l = 1
        minRate = r
        while l <= r:
            mid = l + (r - l) // 2
            # sum the total time it takes with this eating rate
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / mid)
            # now check if totalTime is less than <= h
            if totalTime <= h:
                minRate = min(r, mid) # mid is k in this case
                # slow down eating rate and check if theres a lower value that can eat in that amount of time
                r = mid - 1

            elif totalTime > h: # need to speed up eating rate
                l = mid + 1

        return minRate