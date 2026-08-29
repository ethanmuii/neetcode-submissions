"""
requirements:
- undirected graph meaning edge is bi-directional
- not dense, so use adjacency_list
- nodes labled from 1 to n, so when creating adjacency list need to go from 1 to n + 1
- graph originally had NO CYCLES and CAN WE ASSUME IT WAS CONNECTED?? -> i.e n - 1 edges originally
- according to graph theory, the initial with an added edge will create a cycle. between any number of nodes, could even create multiple different cycles creating multiple paths to get a node (for any number of nodes

constraints:
- guaranteed to be AN EDGE that created a cycle. multiple answers is shown in example 1 since removing an edge could get rid of the cycle, but we want the one that appears last in the input. 
=> intuition hints that we should check if there's a cycle as we build ajacency list?
- WE AREN'T GIVEN n, only the grid edges
- as we are building the adjacency list, how do we specially tell the edge that gets added (currently last in the order) that created the cycle? 
=> if the edges are BOTH already in visited, that means we already have a path to get to both nodes, and adding this new edge creates another path to get these nodes.
=> problem with this solution is that VISITED is global, can't tell if the nodes/edges you've created is all connected 
==> would knowing how many edges we've been through help? we can assume IT WAS all connected
- need to know if what we have added is currently connected or separated


edge cases:
- [[3,4],[1,2],[2,4],[3,5],[2,5]]
###
3: [4]
1: [2]
2: [4]

- its not always the last edge that creates the cycle. 

insight: a cycle is created when 3 nodes have 2 or more inbound/outbound edges. 
"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {i: i for i in range(1, n + 1)}
        for node1, node2 in edges:
            # find leader of node1
            curr = node1
            while parent[curr] != curr:
                curr = parent[curr]

            curr_node = node1
            while curr_node != curr:
                # Remember the next middleman before we overwrite the parent
                next_node = parent[curr_node]
                
                # Flatten: Point this node directly to the ultimate leader
                parent[curr_node] = curr
                
                # Move up to the next middleman
                curr_node = next_node

            # Finally, return the ultimate leader we found
            leader1 = curr
            # find leader of node2
            curr = node2
            while parent[curr] != curr:
                curr = parent[curr]

            curr_node = node2
            while curr_node != curr:
                # Remember the next middleman before we overwrite the parent
                next_node = parent[curr_node]
                
                # Flatten: Point this node directly to the ultimate leader
                parent[curr_node] = curr
                
                # Move up to the next middleman
                curr_node = next_node
            leader2 = curr

            # check if they need to merge or match already
            if leader1 == leader2:
                return [node1, node2]
            else:
                min_leader = min(leader1, leader2)
                if min_leader == leader1:
                    parent[leader2] = leader1
                else:
                    parent[leader1] = leader2
        