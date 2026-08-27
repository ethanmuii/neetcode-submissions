"""
requirements:
- want MIN number of minutes until all cells are either 2 or 0. 

constraints:
- can only move horizontally/vertically from rotten fruit
- fresh fruit becomes rotten every time its adjacent (definition above) from a rottenf ruit
- a fresh fruit(s) is safe if its not connected to any rotten fruit or ANY fresh fruit that is reachable from a rotten fruit. 

solution idea:
- store all rotten fruit in queue (its all starting points). every LEVEL that gets processed is a minute added. every element in the queue is an element is rotten. 
- could modify the grid in place so no need for visited? i.e can only move to fresh fruit? not rotten fruit or empty cell. 
- problem: how do you tell if fresh fruit is still left over? you could count the number of fresh fruit and number of fruit have become rotten durign BFS traversal. if not equal, then return -1 .
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # count the number of fresh_fruit and add rotten_fruit to a queue
        fresh_fruit = 0
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_fruit += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        
        # now add the rotten_fruit to queue
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def in_bounds(r, c):
            return 0 <= r < rows and 0 <= c < cols
        num_minutes = 0
        while queue and fresh_fruit != 0:
            num_minutes += 1
            print(fresh_fruit, len(queue), num_minutes)
            for _ in range(len(queue)):
                dr, dc = queue.popleft()
                for direction in directions:
                    nr = dr + direction[0]
                    nc = dc + direction[1]
                    if in_bounds(nr, nc) and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        fresh_fruit -= 1
                        grid[nr][nc] = 2
    
        if fresh_fruit != 0:
            return -1
        return num_minutes
