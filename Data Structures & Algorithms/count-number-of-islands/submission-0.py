"""
requirements:
- return the nmber of islands (int)

constraints:
- can only go up/down and left/right, no diagonals.
- island doesn't have be to be landlocked like with water in all directions i.e can assume water is surrounding the grid
- to speed it up, don't want to check for possible traversal/islands if we've already visited it. 
=> only want to check for an island when isn't in visited and when you find a possible starting point need to traverse fully to find how big the island is. 

how do you determine an island?
- need to find all adjacent connecting 1s (that patch of 1s is considered one island)
- for another island to be considered separate, it has to be unreachable from top/down/left/right from any other island. 
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def in_bounds(r, c):
            if r >= 0 and r < rows and c >= 0 and c < cols:
                return True
            return False

        for r in range(rows):
            for c in range(cols):
                # start an island search
                if in_bounds(r, c) and (r, c) not in visited and grid[r][c] == "1":
                    visited.add((r,c))

                
                    stack = [(r,c)]
                    # only want to push to stack if its a "1"
                    while stack:
                        dr, dc = stack.pop()
                        for direction in directions:
                            nr = dr + direction[0]
                            nc = dc + direction[1]
                            if in_bounds(nr, nc) and (nr, nc) not in visited and grid[nr][nc] == "1":
                                stack.append((nr, nc))
                                visited.add((nr, nc))

                    num_islands += 1
        return num_islands

