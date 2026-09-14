"""
requirements:
- array is initially unsorted
- return the k-th largest element in the array (if the array were sorted)

constraints:
- finding the k-th largest element in O(n) time, i.e remembering past values you've seen and its priority. usually u could do this with sorting, but want to prevent that -> PQ allows us to remember these values and maintain a sorting invariant for us to later find the k-th largest value

edge cases:
- duplicates are allowed


2 strategies: 
- heapify the whole array to make it a max_heap. and then pop from the array k times and the k-th pop is the answer. 
- as you iterate through the array, add to a min_heap, but only keep it of length k. only add to the min_heap if the current value is greater than the current smallest value. after you finish iterating, it should be 

- 1st option is O(n) while second is O(n log n)
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [num * -1 for num in nums]
        heapq.heapify(nums)
        for _ in range(k):
            top = heapq.heappop(nums)

        return top * -1