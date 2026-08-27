"""
requirements:
- return a list of all valid cells that meet the condition, each cell should be in [r, c] format
- valid cell: water can flow to both pacific and alantic

constraints:
- cell can only go up/down/left/right IF the adjacent cell has lower or equal height
- water can flow into ocean for cells next to ocean? what does that mean??
- starting a TRAVERSAL from every cell in the grid is a big problem??

insights:
- just because a cell is along that path over another cell that can reach doesn't mean it can touch because remember that cell's water can only flow in SPECIFIC DIRECTIONS (not the same as another cell in same path) -> needs to be evaluated on a cell by cell basis?
- could have 2 sets (pacific and alantic) and if a cell is in both that meets it can reach both so its valid
    => elements on the borders arleady get added to sets
- a cell's path has to be constantly decreasing or staying equal, the moment it is surrounded by cells that are all bigger than it and already visited its over. 

- solution idea: is it easier to move from start or from finish? -> start from finish since there is less of them


CORE INSIGHT: instead of viewing as can the cell flood down, VIEW it as can the CELL FLOOD UP to the next cell i.e can the above cell flood down. reversing the flow logic. 
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # helpers:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def in_bounds(r, c):
            return 0 <= r < rows and 0 <= c < cols

        
        atlantic_reachable = set()
        pacific_reachable = set()
        atlantic_stack = []
        pacific_stack = []
        # add all elements starting with pacific
        for c in range(cols):
            pacific_reachable.add((0, c))
            pacific_stack.append((0, c))
        for r in range(1, rows):
            pacific_reachable.add((r, 0))
            pacific_stack.append((r, 0))
        # add all elements starting with alantic
        for c in range(cols):
            atlantic_reachable.add((rows - 1, c))
            atlantic_stack.append((rows - 1, c))
        for r in range(rows - 1):
            atlantic_reachable.add((r, cols - 1))
            atlantic_stack.append((r, cols - 1))

        # do traversal for pacific
        while pacific_stack:
            dr, dc = pacific_stack.pop()
            for direction in directions:
                nr = dr + direction[0]
                nc = dc + direction[1]
                if in_bounds(nr, nc) and (nr, nc) not in pacific_reachable and heights[nr][nc] >= heights[dr][dc]:
                    pacific_reachable.add((nr, nc))
                    pacific_stack.append((nr, nc))

        while atlantic_stack:
            dr, dc = atlantic_stack.pop()
            for direction in directions:
                nr = dr + direction[0]
                nc = dc + direction[1]
                if in_bounds(nr, nc) and (nr, nc) not in atlantic_reachable and heights[nr][nc] >= heights[dr][dc]:
                    atlantic_reachable.add((nr, nc))
                    atlantic_stack.append((nr, nc))



        ans = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    ans.append([r, c])
        return ans

