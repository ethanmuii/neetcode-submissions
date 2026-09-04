"""
requirements:
- n: number of nodes
- what represents each node i.e its index: 1 to n not 0. 
- graph is directed so unidirectional edges. 
- weights are non-negative i.e >= 0
- want the minimum time to reach every NODE.
- k is the node we start at so that should have a time of 0. 

constraints:
- since we want the minimum time for ALL NODES to receive a signal, we have to build an MST
- if the number of total nodes processed is less than total nodes than, return -1
- use kruskal's algorithm as opposed to prim's algorithm since graph is sparse
- OHHH to reach every node, we have to send the signal from a set source value k, and its efficient because then that next node sends its signal to all of its neighbors and updates shortest paths. 
=> in reality, its finding the shortest path from k to every node, but instead of recomputing the simulation each time, it just builds off existing paths and updates/increments it in the actual process. 

edge cases:
- if we are required to start from node k, how do we know which edges start with k as the source? we need to figure otu some way to start with the node with no in_degrees of 0. -> can we assume starting node has no in-degrees?
=> DIJKSTRAS'S
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # need to build the adjacency list that dijkstra depends on
        graph = {i: [] for i in range(1, n + 1)} # value should store dist + node for matching formatting below
        for edge in times:
            u, v, time = edge
            graph[u].append((time, v))
        print(graph)
        
        
        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0
        pq = [(0, k)]

        while pq:
            curr_dist, curr_node = heapq.heappop(pq)
            if curr_dist > distances[curr_node]:
                continue

            for weight, neighbor in graph[curr_node]:
                distance = curr_dist + weight
                # relax
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        for value in distances.values():
            if value == float('inf'):
                return -1

        

        return max(distances.values())
        