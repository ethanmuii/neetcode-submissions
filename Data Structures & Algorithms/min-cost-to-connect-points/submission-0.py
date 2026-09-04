"""
requirements:
- given 2d array where each sublist represents a point [x, y]. 
- calc the distance between 2 points via abs difference
- in a 2-d plane, the graph is UNDIRECTED, edges between 2 points go BOTH WAYS. 
- BUT IT IS WEIGHTED, the weight is the manhatten distance between 2 start points
- want the minimum cost to connect all points together so likely need to build an MST.
=> MST inherently have exactly one path between 2 pair of points, no cycles which means no neg integers.

- graph is DENSE so use prim's. since there can technically be a path between one point and any other point. 

constraints:
- prim's algorithm requires a adjacency list/graph.  so need to build that our first. undirected so values should go in  both

edge cases:



insight:
- dont need to keep track of actual points, it's just used to calc distances, we can convert the poitns representationt o just using node indexs where each point is represented by a node. that's ok since every point should be able to connect to every other point
"""
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {i: [] for i in range(len(points))}
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i].append((dist, j))
                graph[j].append((dist, i))
        visited = [False] * len(points)
        heap = [(0, 0)] # (dist, node), start at node 0 but does not matter
        total_weight = 0
        nodes_visited = 0

        while heap and nodes_visited < len(points):
            dist, node = heapq.heappop(heap)
            if visited[node]:
                continue
            visited[node] = True
            total_weight += dist
            nodes_visited += 1
            for weight, neighbor in graph[node]:
                if not visited[neighbor]:
                    heapq.heappush(heap, (weight, neighbor))

        return total_weight if nodes_visited == len(points) else -1



        # build adjacency list/graph, its basically building a 2d list to every possible combination
        graph = {(x, y): [] for x,y in points} # (x,y) is the key, and value is (manhatten distance, point)
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                # now create the undirected edge with the dist
                graph[(points[i][0], points[i][1])].append((dist, (points[j][0], points[j][1])))
                graph[(points[j][0], points[j][1])].append((dist, (points[i][0], points[i][1])))

        visited = False 