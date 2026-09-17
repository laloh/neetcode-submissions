class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board or not board[0]:
            return
        
        ROWS, COLS = len(board), len(board[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(r, c, board):
            if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) 
                or board[r][c] != "O"):
                return
            
            board[r][c] = "#"
            dfs(r + 1, c, board)
            dfs(r - 1, c, board)
            dfs(r, c + 1, board)
            dfs(r, c -1, board)


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    dfs(r, c, board)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"

        