class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        ROWS, COLS = len(grid), len(grid[0])
        Treaqueue = deque()
        INF = 2147483647


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    Treaqueue.append((r, c))
        
        while Treaqueue:
            r, c = Treaqueue.popleft()

            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = dr + r , dc + c
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    Treaqueue.append((nr, nc))
        