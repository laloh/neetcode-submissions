class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def backtrack(r, c, k):
            print(path)
            if k == len(word):
                return True
            
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                word[k] != board[r][c] or (r, c) in path):
                return False
            
            path.add((r,c))

            res = (backtrack(r + 1, c, k + 1) or
                  backtrack(r - 1, c, k + 1) or
                  backtrack(r, c + 1, k + 1) or
                  backtrack(r, c - 1, k + 1))

            # CORRECCIÓN 1: Remover la coordenada específica, no una aleatoria
            path.remove((r, c))
            
            # CORRECCIÓN 2: Tienes que retornar el resultado de la exploración
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0): return True
        
        return False