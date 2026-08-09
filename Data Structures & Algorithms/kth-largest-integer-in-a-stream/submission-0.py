"""
- brute force way to find the specific value that meets a priority like largest or smallest is to sort (i.e creates an invariant)

only return the kth largest value after you add a value

ideally, would not want to sort elements on initialization or after each add => priority queue
"""
import copy
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k # this doesn't change after intialization
        self._max_queue = [] # need to multiply by -1 for it to be a max queue. heapq is inherently min queue
        for num in nums:
            heapq.heappush(self._max_queue, -1 * num)


    def add(self, val: int) -> int:
        # need the value to the original max_queue
        # how can you see the kth-largest value in priority queue without popping it from original queue, need to make a copy?
        heapq.heappush(self._max_queue, -1 * val)
        temp = copy.copy(self._max_queue)
        for _ in range(self._k):
            value = heapq.heappop(temp)
        return value * -1