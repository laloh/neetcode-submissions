class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = {}


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        ROWS, COLS = len(board), len(board[0])
        root = TrieNode()

        for word in words:
            curr = root     
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word

        res = []
        def backtrack(r, c, root):
            char = board[r][c]
            root = root.children[char]

            if root.word:
                res.append(root.word)
                root.word = None
            
            board[r][c] = "#"

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != "#" and board[nr][nc] in root.children:
                    backtrack(nr, nc, root)

            board[r][c] = char


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    backtrack(r, c, root)
        

        return res