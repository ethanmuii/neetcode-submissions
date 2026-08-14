"""
remember: 
- board[0] represents a row. and board[0][i] represents a column in a row. 
- cols move you left or right and rows move you up or down

requirements:
- return true if your curr_path is equal to word, and default to false if it can't find it after backtracking and recursing every subpath through the grid. 

constraints:
- can only go horizontally/vertically, no diagonals and must be within boundary of the grid. 
- how do you stop early once you've found the word

# base case:
- curr_path after combined via .join is equal to word, and only do this work if curr_path is len(word) long.
- if curr_path is > len(word), no need to keep recursing because this path won't lead us to the right solution so you can stop


edge cases:
- this is a permutation problem sine the order in where the letter appears matter. 
=> each letter is the new branch of a path and the places and orderings are determined by which directions you go until the word is 4 letters long.
=> you need to either go to that letter and include it or don't go to that letter and don't include it. 
=> backtrack starts at top left of board so board[0][0]
- how do we efficiently not check duplicates orderings??
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] # right, left, up, down

        def backtrack(row, col, curr_path):

            if len(curr_path) == len(word) and "".join(curr_path) == word:
                return True
            elif len(curr_path) > len(word):
                return
            for direction in directions:
                if ((row + direction[0], col + direction[1]) not in visited) and 0 <= row + direction[0] < len(board) and 0 <= col + direction[1] < len(board[0]):
                    curr_path.append(board[row + direction[0]][col + direction[1]])
                    visited.add((row + direction[0], col + direction[1]))
                    is_found = backtrack(row + direction[0], col + direction[1], curr_path)
                    curr_path.pop()
                    visited.remove((row + direction[0], col + direction[1]))
                    if is_found:
                        return True

        for r in range(len(board)):
            for c in range(len(board[0])):
                visited = set()
                visited.add((r, c))
                is_found = backtrack(r, c, [board[r][c]])
                if is_found:
                    return True
        return False