class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])


        def dfs(r, c):
            grid[r][c] = "#"

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                    dfs(nr, nc)

        cnt = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    cnt += 1
        
        return cnt