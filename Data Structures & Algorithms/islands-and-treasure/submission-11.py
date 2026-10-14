class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        INF = 2147483647

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))

        
        while queue:
            r, c, dist = queue.popleft()
            
            for dr, dc in [(0, 1), (1, 0), (-1, 0) ,(0, -1)]:
                nr, nc = dr + r, dc + c
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                    grid[nr][nc] = dist + 1
                    queue.append((nr, nc, grid[nr][nc]))    
        
        print(grid)