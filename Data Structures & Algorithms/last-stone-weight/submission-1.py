"""
requirements:
- need to return a specific value depending if there's one stone or zero stones which is return 0 - check len of pq
- given an array of integers that represents the weight of each stone

constraints:
- from this array, we want the two heaviest stones for an iteration. how to find that in O(log) time? -> use pq
- if the 2 heaviest stones are equal, do nothing, we can leave those 2 popped and start next iteration
- if one stone (X) is less than y, then x is destoryed and the stone y is added back to queue with y - x. 
=> given the conditions, i assume x means second heaviest, and y means first heaviest

- need the heaviest stones so need it to be -1
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while stones:
            print(stones)
            if len(stones) == 1:
                return stones[-1] * -1

            y = heapq.heappop(stones) * -1
            x = heapq.heappop(stones) * -1
            if x < y:
                heapq.heappush(stones, (y - x) * -1)

        return 0