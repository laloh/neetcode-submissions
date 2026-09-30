class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid:
            return -1
        
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        fresh_fruit = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                
                if grid[r][c] == 1:
                    fresh_fruit += 1

        time = 0
        while queue and fresh_fruit > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh_fruit -= 1
                
            time += 1

        print(time, fresh_fruit)    
        return time if fresh_fruit == 0 else -1
    