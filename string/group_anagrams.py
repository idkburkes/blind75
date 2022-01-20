from collections import Counter


# Very pythonic solution
# Time complexity O(n * mlogm)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            key = tuple(sorted(word))
            res[key] = res.get(key, []) + [word]
        return list(res.values())
        
        