"""
- same concept as the number of islands but count the size of the island as you go through all of stack and then update it if its a max?
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # make in bounds function
        def in_bounds(r, c):
            return 0 <= r < rows and 0 <= c < cols

        for r in range(rows):
            for c in range(cols):

                if in_bounds(r, c) and (r,c) not in visited and grid[r][c] == 1:
                    visited.add((r,c))
                    stack = [(r,c)]
                    size = 0
                    while stack:
                        dr, dc = stack.pop()
                        size += 1
                        for direction in directions:
                            nr = dr + direction[0]
                            nc = dc + direction[1]
                            if in_bounds(nr, nc) and (nr, nc) not in visited and grid[nr][nc] == 1:
                                visited.add((nr, nc))
                                stack.append((nr, nc))

                    max_area = max(max_area, size)

        return max_area