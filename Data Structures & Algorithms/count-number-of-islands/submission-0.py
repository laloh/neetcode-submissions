class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        def is_within_bounds(r, c, grid):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
            
        def dfs(r, c, grid):
            grid[r][c] = "-1"
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for d in dirs:
                next_r, next_c = r + d[0], c + d[1]
                if is_within_bounds(next_r, next_c, grid) and grid[next_r][next_c] == "1":
                    dfs(next_r, next_c, grid)

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c, grid)
                    count += 1
        
        return count