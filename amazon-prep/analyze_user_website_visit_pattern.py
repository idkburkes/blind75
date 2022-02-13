from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        TUW = tuple(zip(timestamp, username, website))
        TUW = sorted(TUW)
        
        user_history = dict()
        for time, user, website in TUW:
            user_history[user] = user_history.get(user, list())
            user_history[user].append(website)
        
        pattern_count = dict()
        for user in user_history.keys():
            for comb in set(combinations(user_history[user], 3)):
                pattern_count[tuple(comb)] = pattern_count.get(tuple(comb), 0) + 1
        
        def key_sort(pattern):
            return (-pattern_count[pattern], pattern)
        
        return sorted(pattern_count,key =key_sort)[0]
        
        
        
            
        