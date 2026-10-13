class Solution:
    def __init__(self):
        self.max_area = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            grid[r][c] = "#"

            area = 1

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = dr + r, dc + c
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != "#" and grid[nr][nc] == 1:
                    area += dfs(nr, nc)

            return area

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    res = max(area, res)

        return res