class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return
        
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                
                if grid[r][c] == 1:
                    fresh += 1
        
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        mins = 0
        while queue and fresh > 0:
            mins += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
        print(fresh)
        return mins if fresh == 0 else -1