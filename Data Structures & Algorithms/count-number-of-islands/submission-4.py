class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        
        visited = set()
        def dfs(r, c):
            if r >= ROWS or c >= COLS or grid[r][c] == "0" or (r, c) in visited:
                return

            visited.add((r, c))

            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != "0":
                    dfs(nr, nc)

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r, c)
                    islands += 1
    
        return islands