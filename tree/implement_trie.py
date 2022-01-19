class TreeNode:
    
    def __init__(self, char):
        self.char = char
        self.children = dict()

class Trie:

    def __init__(self):
        self.root = TreeNode('ROOT')
        
    def insert(self, word: str) -> None:
        if word is None: return
        cur = self.root
        for letter in word:
            if letter in cur.children:
                cur = cur.children[letter]
            else:
                cur.children[letter] = TreeNode(letter)
                cur = cur.children[letter]
        cur.children['TAIL'] = TreeNode('TAIL') #mark this as the ending of a word
            
        
    def search(self, word: str) -> bool:
        if word is None: return False
        if not len(word): return True
        cur = self.root
        for letter in word:
            if letter in cur.children:
                cur = cur.children[letter]
            else:
                return False
        return 'TAIL' in cur.children
            
        

    def startsWith(self, prefix: str) -> bool:
        if prefix is None: return False
        if not len(prefix): return True
        cur = self.root
        for letter in prefix:
            if letter in cur.children:
                cur = cur.children[letter]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)