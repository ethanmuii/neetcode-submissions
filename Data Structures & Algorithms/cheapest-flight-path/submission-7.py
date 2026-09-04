"""
requirements:
- each node is represented by 0, n - 1   i.e that's its index // 'n' total nodes though
- graph is directed i.e flights are represented with src, dst and its a one-way flight, NOT BIDIRECTIONAL
- graph is weighted since each edge has a "COST"




constraints:
- can assume no src,dst equals each other for the final answer
- can assume flights are unique (u, v) connection can be used once. -> prevents from having to check for cheapest priced between a direct flight between u, v i.e 2 flights have different prices for same src, dst combination. 

- shortest path is defined by min/cheapest price from our starting node to the node we are trying to reach
- k stops represents the "internal" or middle-man nodes that we may have to stop at between us reaching dst from src. => i.e any flight where the destination is NOT DST.
=> a direct flight from src to dst is technically 0 stops used. 

insights:
- thinking djistra's algo, however, how do we handle k constraint. add number of stops used to get to this node in the heap? still want the cheapest flights so that should be the primary sorter, but then do number of stops.
=> since heap is inherently min_queue, we would want the stops_used to get here to be the lowest it can be as the second tie breaker
=> then for informational pruposes, the actual dst node of that flight. 

=> when we add it to heap, should it be number of stops used to get here like when should we increment number of stops after we pop from the heap or when we push to heap? 
=> if we pop an edge from a heap and its destination is our destination, then we return total cost and break. 
=> if the destination is not our destination, we would need to increment stops before we push the value to queue.
=> number of stops should be incremented at push to queue time, not after pop fromm queue time. 

=> skip if its a node we already visited? or is that not the main constrant, instead skip if the number of stops would be greater than k. => or we can prevent that all together by not adding flights that would put our value over k



- need to build ajacency list first



edge case:
- there may be a cheapest path to dst node, but it requires more than k stops. => THIS ANSWER should not be returned.
=> thinking about theoretically, 1) want all possible paths from src to dst that take a max of k stops. 
=> 2) then from those paths, we want the cheapest one. 


we can handle the k constraint by not adding an edge if it would put our used_stops over k. do we also have to check where the flight itself is going?
=> do we want to handle that after the pop or insertion
=> handle it on the insertion, its how you scope out any edges that would not create valid paths of less than k stops

=> number of stops should only increment if the dst is not our expected
=> the problem is that used_stops should be at max equal 1 to reach dst. if you are adding a stop to reach another node that isn't dst then that's not allowed. a stop should only be incremented if 


edge case:
- do not want to update the cheapest path to get to a node if the path it took to get to that node (not necessarily dst node) is more than k stops. this messes up our comparison for not checking a path to a node if it more expensive. but just because its more expensive is not inherently bad. it just can't be more than k stops to reach there.
=> need to move up constraint checking to handle checking number of stops used before we update the the cheapest option to get to a node. 

MY BIGGEST PROBLEM IS HANDLING not incrementing number of stops used if our destination is dst. 
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # build adj list
        graph = {i: [] for i in range(n)}
        for source, destination, cost in flights:
            graph[source].append((cost, destination))

        
        best_stops = {i: float('inf') for i in range(n)}
        best_stops[src] = 0
        pq = [(0, 0, src)] # (cost, number of stops used to get here, dst)

        while pq:
            curr_cost, used_stops, curr_src = heapq.heappop(pq)
            if used_stops > best_stops[curr_src]:
                continue

            best_stops[curr_src] = used_stops

            if curr_src == dst:
                return curr_cost

            for cost, neighbor in graph[curr_src]:
                distance = curr_cost + cost
                if used_stops <= k:
                    heapq.heappush(pq, (distance, used_stops + 1, neighbor))


        return -1