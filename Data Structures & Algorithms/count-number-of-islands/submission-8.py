class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            char = grid[r][c]
            grid[r][c] = "#"

            for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                nr, nc = dr + r, dc + c
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != "#" and grid[nr][nc] == "1":
                    dfs(nr, nc)
            
        
        num_islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    num_islands += 1
        
        print(grid)

        return num_islands