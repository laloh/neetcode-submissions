class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c):
            grid[r][c] = "#"

            area = 1
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    area += dfs(nr, nc)
                
            return area
    
        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    cnt = dfs(r, c)
                    max_area = max(max_area, cnt)

        return max_area