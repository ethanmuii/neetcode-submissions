"""
requirements:
- input comes in a 2d array where each sublist is of length 2 and is [xi, yi]
- want the k closest points to point [0,0]
- to find the k closest points to (0, 0), we want to calculate the distance of every point to (0,0)

constraints:
- to remember the values we calculated AND know the k closest points in O(1) time, we would want to use a pq. the pq allows us to make an invariant and access them in O(1) time
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_pq = []
        for point in points:
            distance = math.sqrt((0 - point[0])**2 + (0 - point[1])**2)
            heapq.heappush(min_pq, (distance, point))

        ans = []
        for _ in range(k):
            top = heapq.heappop(min_pq)
            ans.append(top[1])
        return ans