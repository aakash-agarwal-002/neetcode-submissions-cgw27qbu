class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEnd = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.isEnd = True
            

    def search(self, word: str) -> bool:
        def dfs(word,root):
            curr = root
            for i in range(len(word)):
                w = word[i]

                if w == ".":
                    for child in curr.children.values():
                        if dfs(word[i+1:],child):
                            return True
                    return False
                else:
                    if w not in curr.children:
                        return False
                    curr = curr.children[w]
            return curr.isEnd

        return dfs(word,self.root)
         
 
        
