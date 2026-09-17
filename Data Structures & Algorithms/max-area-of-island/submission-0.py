class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0


        def dfs(r, c, grid):
            grid[r][c] = -1

            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            area = 1
            for d in dirs:
                next_r, next_c = r + d[0], c + d[1]
                if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]) and grid[next_r][next_c] == 1:
                    area += dfs(next_r, next_c, grid)
                
            return area
            
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res = dfs(r, c, grid)
                    max_area = max(max_area, res)
                    # calculate the area

        return max_area