class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True
    
    def search(self, word: str) -> bool:
        def dfs(root, index):
            for i in range(index, len(word)):
                char = word[i]

                if char == ".":
                    for child in root.children:
                        if dfs(root.children[child], i + 1):
                            return True
                    return False
        
                if char not in root.children:
                    return False                    

                root = root.children[char] 

            return root.is_end

        return dfs(self.root, 0)