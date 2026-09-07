"""
requirements:
- stream of values is just an array. 
= INCLUDES DUPLICATES
= NOT ORIGINALLY SORTED


constraints:
- to find kth largest elements, need a max queue to look at largest elements.so need to multiply -1 on addition, and when we return a value multiply by -1 to get the actual value.

- k stays the same for the whole class instance. it doesn't change after/on 'add'.
- on add, you have to make sure to add it BEFORE YOU check the k-th largest integer.
=> you have to make sure that STATE GETS RETURNED BACK TO NORMAL AFTER YOU FIGURE OUT THE k-th largest elements. you don't pop values to find the k-th largest, and then the stream stays like that, you have to return it normal. 
=> It becomes O(k) separate loops in every add
"""
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.k = k
        for num in nums:
            heapq.heappush(self.pq, num * -1)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val * -1)
        add_back = []
        for i in range(self.k):
            curr = heapq.heappop(self.pq)
            add_back.append(curr)
        for num in add_back:
            heapq.heappush(self.pq, num)
        return curr * -1

