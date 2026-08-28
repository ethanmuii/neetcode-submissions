"""
requirements:
- m x n board, contains X or O.
- regions can be any shape. region is just group of connected 'O' cells. (touching diagonally does not count)
- only surrounded regions can be captured i.e capture = replace all the O's with X's.
- region is safe if A CELL OR MORE in the region is touching the edge. 

constraints:
- can only move up/down/left/right
- want to modify IN-PLACE. 

insights:
- brute force: traversing through every possible cell only if its not visited and its an O. 
=> could require visiting the same cells over again?
- start with all O's, add any O's to its queue to continue the search only if its connected to X
- editing in place lets us know that this O has been captured b/c we changed it to an 'X', but we don't know if that region is later connected to an O on the board. 
- PROBLEM: if you start with the boundaries, you don't know if that region could LATER be connected to an 'O' that is on the edge. i.e edge case 1 => can't start with all boundary points being the queue. + can't let them just keep on overwriting themselves.
- start with all O's on the edge, any O's that it can reach are within its region and should stay the same. and at the end any O's that are not VISITED should be switched to X's? 
=> that would be a lot of for loops but still O(m x n)?

-


edge cases
- board=[["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","O","X","X"]]

"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        def in_bounds(r, c):
            return 0 <= r < rows and 0 <= c < cols

        # add all O's that are on the edge
        visited = set()
        stack = []
        for r in [0, rows - 1]:
            for c in range(cols):
                if board[r][c] == "O":
                    visited.add((r, c))
                    stack.append((r, c))

        for r in range(1, rows - 1):
            for c in [0, cols - 1]:
                if board[r][c] == "O":
                    visited.add((r, c))
                    stack.append((r, c))
        
        # now iterate and add all O's that are connected to any boundary O as visited and safe. 
        while stack:
            dr, dc = stack.pop()
            for direction in directions:
                nr = dr + direction[0]
                nc = dc + direction[1]
                if in_bounds(nr, nc) and (nr, nc) not in visited and board[nr][nc] == "O":
                    stack.append((nr, nc))
                    visited.add((nr, nc))
        # now iterate through the board modify any O's that are not visited
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and board[r][c] == "O":
                    board[r][c] = 'X'


        return