"""
requirements:
- need to edit inputs as we traverse. allowed since the actual dimensions of the list aren't changing
- 3 separate expected values: inf, 0, -1

constraints:
- can only go left, down, up, right
- if a land cell cannot reach a treasure chest then it should keep its value, but we need to know that we at least tried to reach a treasure chest so mark it as visited
- want the distance to nearest treasure chest i.e USE BFS. 
- should perform/start BFS at each land cell since we want the closest treasure chest to each land cell. 
=> if can't reach a treasure chest then keep it same and add it to visited. 
- once you have found a treasure chest in a land's traversal, break from the queue (BFS) and update its value the land value to be its distance from it. 
- only continue traversing if its land. there needs to be a separate visited set for land starting points and separate lands traversed in a traversal?
=> OR just add all the possible starting points to a list and start the traversal for each. 


new solution idea:
- problems with old: modifying the grid values in place caused some islands to not reach treasure chest in optimal way / required us to store a visited SET for each possible starting point, and storing the land has possible starting points made us re-visit cells over and over again since you are finding it for each land's path.

- what if we started from the treasure chests and did BFS for treasure chests at the same time. so each "level" is all the lands away from any treasure chest. and dist is global and visited is also global. additionally, this guarantees that earlier land values don't overwrite later ones since it goes outwards. 


"""
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        queue = deque()

        # store all start points
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def in_bounds(r, c):
            return 0 <= r < rows and 0 <= c < cols

        # now begin BFS traversal
        dist = 1 # everything will be 1 away from treasure chest
        while queue: 
            for _ in range(len(queue)):
                dr, dc = queue.popleft()
                for direction in directions:
                    nr = dr + direction[0]
                    nc = dc + direction[1]
                    # check if not visited and if its land => mark visited, modify in place, and append its coords to grid
                    if in_bounds(nr, nc) and (nr, nc) not in visited and grid[nr][nc] == 2147483647:
                        visited.add((nr, nc))
                        grid[nr][nc] = dist
                        queue.append((nr, nc))
            dist += 1
        return




                
            
        