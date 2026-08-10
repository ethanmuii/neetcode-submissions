"""
2 ways to do this

first solution:
- heapify all elements of nums and make it be a max heap.
- to find the kth largest element in the array, pop from the max heap k times and you will find the kth largest element in the whole array

- time complexity becomes O(n) and space complexity becomes O(n)

second solution:
- use a min heap and only allow k elements in the min-heap. 
- you want to have the largest elements in the min heap, and the min heap be of length k so the k-th largest element is actually the smallest element in the largest k elements. 
- go through all the elements, and if the new element is larger than the smallest element, then pop it and append the larger element
-> leaves you with the largest k elements in the array (getting rid of the smaller one each time) and then the top one is the k-th largest element

- time complexity is O(n log k) cuz you have iterate through each element and pushing takes log k times to push to a priority queue of length k. space complexity is O(k) though. 


for better time complexity, lets go with first olution
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        for _ in range(k):
            value = heapq.heappop(max_heap)

        return -1 * value