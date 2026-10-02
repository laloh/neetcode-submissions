class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])
        queue = deque()
        
        for r in range(ROWS):
            if board[r][0] == "O":
                queue.append((r, 0))
            if board[r][COLS - 1] == "O":
                queue.append((r, COLS - 1))

        for c in range(COLS):
            if board[0][c] == "O":
                queue.append((0, c))
            if board[ROWS - 1][c] == "O":
                queue.append((ROWS - 1, c))

        while queue:
            r, c = queue.popleft()
            
            if board[r][c] == "O":
                board[r][c] = "T"

            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = dr + r, dc + c
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O":
                    queue.append((nr, nc))


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

                if board[r][c] == "T":
                    board[r][c] = "O"



