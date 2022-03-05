

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = []
               
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node.children[char].words.append(word)
            node.children[char].words.sort()
            if len(node.children[char].words) > 3:
                node.children[char].words.pop(3)
            
            node = node.children[char]
            
    def search(self, word):
        node = self.root
        res = []
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            res.append(node.words)
        l_remain = len(word) - len(res)
        for _ in range(l_remain):
            res.append([])
            
        return res
            
                
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for prod in products:
            trie.insert(prod)
        
        return trie.search(searchWord)
        