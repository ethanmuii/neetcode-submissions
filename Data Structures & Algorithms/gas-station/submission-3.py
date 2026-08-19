"""
requiremnts:
- given 2 arrays
- last index always wraps around to first index!! similiar to how -1 goes to last station, but len(array) - 1 goes to 0 next. 
- tank = 0 at start, can store extra gas (no constraint on gas)
- GOAL: return THE CORRECT starting gas station index that would allow you to do one full loop i.e from start to end. 
=> whereever you start, you must also be able to reach the end of. i.e start at 3, must have enough gas to get to 3 when you are at 2. 
=> ONLY one correct index or NO correct index
=> either you find the only correct solution and can stop or you gotta keep on trying to confirm its impossible and return -1. => RETURNING THE INDEX itself. 

constraints:
- brute force would be to just try every index i.e O(n^2) for each index start at it, and go around at max once again for each index to see if its completable. 
- cant sort the arrays or combine and sort would be O(n log n). and since the order you visiting matters. 

insights:
- when can you get to the next station? -> if your current tank + gas[i] is >= cost[i], you can get to the next station. if its not, its a dead end and move to next possible starting index.
- can you prune earlier? 
- how to efficiently do the wrap around -> modulo indexing? 

brute force doesn't work because ideally you shouldn't have to try every index (you get time limit exceeded)
=> what if you know you can reach all the way around at the specific index that gas is greater than cost, if its never greater than cost then its -1. => doesn't work b/c of this edge case: gas=[1,2,3,4,5]
cost=[3,4,5,1,2]


what can you conclude after checking an index? -> so you don't have to check every index or know what index to specifically check?
=> IF YOU START AT A SPECIFIC INDEX but it fails at a station B, then you don't even have to check starting stations A through B - 1. and you need to start checking a start at B. This is because A + 1 or A + 2 will only give you less gas not more. this is because A is guaranteed to be positive, not negative so the lowest you could have is 0. 

edge cases:
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start_index = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i]

            tank -= cost[i]
            if tank < 0: 
                tank = 0
                start_index = i + 1

        return start_index
        