class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()
        
        def dfs(r, c, visit):
            if (r, c) in visit:
                return
            
            visit.add((r, c))

            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visit)

            
        
        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS - 1, atl)

        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS - 1, c, atl)
        
        return list(atl.intersection(pac))