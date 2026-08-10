"""
- given an array of integers
- at each interval/step, we need to get 2 HEAVIST stones -> think priority queue! -> allows easiest access for max/min of a list.

1st condition: x = y, so those stones can be "deleted/ignored" -> go to next interval
2nd condition: x < y, weight x is deleted and the stone of weight y is added back to queue with y - x

is x the first stone? or is y the first stone

keep the intervals going while len(pq) > 1

return the 1 stone in the pq at the end or return 0 if none remain

- two heavist stone means max pq
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # initialize the pq
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while max_heap and len(max_heap) > 1:
            one = heapq.heappop(max_heap)
            two = heapq.heappop(max_heap)
            if -two < -one:
                heapq.heappush(max_heap, -(-one - -two))
        if max_heap:
            return max_heap[0] * -1
        else:
            return 0