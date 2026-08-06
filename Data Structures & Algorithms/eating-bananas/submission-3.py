"""
problem notes:
- we have to eat sum(piles[i])
- can only eat from 1 pile of bananas per hour regardless of whether
=> we finish that pile, leave bananas leftover, or overeat from that pile (i.e our k is > piles in/left in the pile)

given h (hours), what is the slowest we can eat per hour where we finish all the bananas earlier or by h
=> i.e we want to take up as close to h as possible and finish the bananas
=> if we can finish the bananas before h by a lot or at all, check if we can make the k lower. 

more insights:
- h hours must be at least equal to number of piles. -> this is because we can only eat from 1 pile per hour
=> if there is less hours than number of piles, then we cannot eat all the bananas since we cannot eat multiple piles in 1 hr no matter the eating rate


=> since we can only eat from 1 pile per hour, the fastest we can eat all the bananas is 
=> max(piles) which is the max number in piles. 
=> this is because if we are eating at a rate of the highest number of bananas in the pile
=> and we have at least len(piles) to eat we will finish every pile in 1hr which is also the "at least" or bare minimum amount of time we can eat all bananas

solution: what if we preformed a binary search from 0 to the fastest time? 
that is our range for eating rate

if we can eat the bananas with k = midpoint then lower the range for k
if we cannot eat the banas with k = midpoint then increase the range for k
do this until we find the min number for k which will be found once l > r.
until this condition is reached there's a possible "minimum-er" value. 
"""
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = max(piles)
        l = 1
        r = minSpeed

        while l <= r:
            mid = l + (r - l) // 2
            # calc the number of hours it takes to eat with this eating speed
            # is there any way you know if your hours will be less than given hours just by eating speed in O(1)?
            currHours = 0
            for pile in piles:
                currHours += math.ceil(pile / mid)
                if mid == 16:
                    print("time", pile / mid)
                    print(currHours)
            if currHours <= h:
                minSpeed = min(minSpeed, mid)
                r = mid - 1
            else:
                l = mid + 1

        return minSpeed
        