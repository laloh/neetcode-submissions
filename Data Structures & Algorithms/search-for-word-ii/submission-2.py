class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.root
        ROWS = len(board)
        COLS = len(board[0])

        # Build Trie
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word
        
        res = []

        def backtrack(r, c, board, parent_node):
            char = board[r][c]
            curr = parent_node.children[char]

            # Avoid duples
            if curr.word:
                res.append(curr.word)
                curr.word = None

            board[r][c] = "#"

            for dr in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = r + dr[0], c + dr[1]
                if 0 <= nr < ROWS       and \
                   0 <= nc < COLS       and \
                   board[nr][nc] != "#" and \
                   board[nr][nc] in curr.children:
                   backtrack(nr, nc, board, curr)
            
            board[r][c] = char

            if not curr.children:
                del parent_node.children[char]


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    backtrack(r, c, board, root)

        return res