"""
question: what is the lowest you can make k (bananas per hour) to eat all of the bananas in the array BEFORE it reaches H

- you can't just add up all of the piles and then divide by the number of hours you have for k
=> this is because some piles might take 2 hours of k to finish the pile, not always 1. which the above equation assumes.
=> pile of bananas / k = # of hours it takes for that pile

- answer doesn't consider decimals
- if you are gonna overeat for a pile, you might as well overeat as long as you are under number of hours

based on examples, it looks k is one of the numbers in piles. you want k to be the minimum number it can be (chosen from one of the piles) while the number of hours still being under time
- O(n^2) would be to try each number as k and then see how much time it would take for each pile as that k and keeping the minimum pile number that meets valid condition. 
=> THIS DOESN'T WORK EITHER. one of the later edge cases proves this theory wrong.
=> [3, 6, 7, 11] and h = 8 proves this wrong. -> understand why. 

**HOW CAN WE NARROW DOWN THE SEARCH RANGE OF POSSIBLE VALUES k'values that meet h condition?**
**how can we keep on going until we find the lowest k, an integer, that meets this condition**

- since we can only eat from 1 pile per hour, a reasonable maximum k value is the max value of all piles.
=> hours cannot be less than number of piles -> the fastest you can eat the number of piles is max of number of piles -> only takes you 1 hour to each all piles 
=> if you can eat the max pile in 1 hour, you can eat the rest of the piles in 1 hour each as well.

- the lowest K can be is 1. since only integer values are allowed for k and zero not being valid is obvious.
=> this case only works if sum(piles) == h where you can eat 1 banana from the total number of piles and it will still be equal to hours. 
"""
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sortedPiles = sorted(piles)
        minK = sortedPiles[-1]
        l = 1
        r = sortedPiles[-1]
        while l <= r:
            mid = l + (r - l) // 2 # proposed k value
            hourCounter = 0
            for val in sortedPiles:
                hourCounter += math.ceil(val / mid)
            if hourCounter <= h:
                # midpoint could be less meaning slower eating rate to take up more time
                if mid < minK:
                    minK = mid
                r = mid - 1
            elif hourCounter > h: 
                # midpoint needs to be faster eating rate to use up less than time
                l = mid + 1
                # we found our minimum eating rate k. if we make it midpoint any slower, its past h. 
                # but sometimes the minimum eating rate k will be slightly less than h
                # => but that shouldn't mean make eating rate slower by 1 cuz that might take up past h.
                # need to make end condition handle that case. 

                # basically shrinking search condition until we've checked everything that the minimum k could work
        return minK