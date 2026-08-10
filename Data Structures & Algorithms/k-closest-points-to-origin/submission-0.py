"""
- k represents the number of points in our answer
- closest keyword -> want min heap -> want to minimize distance
- data type: each point is represented as a list where list[0] is x and list[1] is y. -> this is in another list so a list of coordinates

- want to store the distance from each point to (0, 0) in the priority queue, however our answer should be a list of points.
=> 2 options, either use a hash map to make the lookup between points and distance a O(1) time operation or just pass a the point itself as the second element in the tuple where the first element is the distance. => answer is guaranteed to be unique so possibly it wouldn't break at the tie breaker if 2 points are equal distant and it tries to compare coordinates itself
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # create a heap and add all elements to the heap
        min_heap = []
        for point in points:
            distance = math.sqrt((0 - point[0])**2 + (0 - point[1])**2)
            heapq.heappush(min_heap, (distance, point))

        # everything is now in the heap, we want to pop k elements and append them to list and return list
        ans = []
        for _ in range(k):
            value = heapq.heappop(min_heap)
            ans.append(value[1])
        
        return ans