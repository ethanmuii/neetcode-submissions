"""
requirements: 
- given a list of ints, each int represents a pile of bananas
- must eat all of the bananas and thus piles in a maximum of h hours. 
- what is the slowest rate of k you can eat to achieve this in maximum of h hours?
=> thus, what is the slowest rate where we eat all of the bananas just below or at h hours of time? 
=> if we take too much time, increase k
=> if we take too little time, decrease k. => keep on decreasing k until the # of hours is still less than h, but as close to h as possible 

=> this problem sounds like binary search

slowest rate is 1 banana per hour?
fastest rate is biggest pile in piles. we can only eat 1 pile per hour so the fastest we can eat all bananas is each a whole pile an hour. to succesfully eat a whole pile, we need to be able to eat the biggest pile 
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minSpeed = r
        while l <= r:
            midpoint = l + (r - l) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / midpoint)
            if time <= h:
                r = midpoint - 1
                if midpoint < minSpeed:
                    minSpeed = midpoint
            elif time > h:
                l = midpoint + 1
        
        return minSpeed