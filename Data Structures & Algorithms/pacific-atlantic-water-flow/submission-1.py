class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()
        
        def dfs(r, c, visit, prevHeight):
            if (r, c) in visit or heights[r][c] < prevHeight:
                return
            
            visit.add((r, c))

            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    dfs(nr, nc, visit, heights[r][c])

            
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        return list(atl.intersection(pac))