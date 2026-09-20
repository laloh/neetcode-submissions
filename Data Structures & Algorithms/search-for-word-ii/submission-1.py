class TrieNode:
    def __init__(self):
        self.is_end = False
        self.word = None
        self.children = {}

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        root = TrieNode()

        # Build the trie
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word

        res = []
        def backtrack(r, c, parent_node, board):
            char = board[r][c]
            curr_node = parent_node.children[char]

            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None

            board[r][c] = "#"

            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for _dir in dirs:
                nr, nc = r + _dir[0], c + _dir[1]

                if (0 <= nr < rows and 0 <= nc < cols and 
                    board[nr][nc] != "#" and 
                    board[nr][nc] in curr_node.children):
                    backtrack(nr, nc, curr_node, board)

            board[r][c] = char

            if not curr_node.children:
                del parent_node.children[char]

        for ROW in range(rows):
            for COL in range(cols):
                if board[ROW][COL] in root.children:
                    backtrack(ROW, COL, root, board)

        return res
        