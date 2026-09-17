class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        r_len = len(grid)
        c_len = len(grid[0])
        
        def dfs(r, c, grid):
            grid[r][c] = "-1"
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for d in dirs:
                next_r, next_c = r + d[0], c + d[1]
                if (0 <= next_r < len(grid) and 0 <= next_c < len(grid[0])) and grid[next_r][next_c] == "1":
                    dfs(next_r, next_c, grid)

        count = 0
        for r in range(r_len):
            for c in range(c_len):
                if grid[r][c] == "1":
                    dfs(r, c, grid)
                    count += 1
        
        return count
        
      