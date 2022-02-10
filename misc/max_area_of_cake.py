

def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
    hcuts = sorted(horizontalCuts)
    vcuts = sorted(verticalCuts)
        
    hcuts.insert(0, 0)
    hcuts.append(h)
    vcuts.insert(0, 0)
    vcuts.append(w)
    
    max_height = 0
    for i in range(len(hcuts)-1):
        max_height = max(max_height, hcuts[i+1] - hcuts[i])
    max_width = 0
    for i in range(len(vcuts)-1):
        max_width = max(max_width, vcuts[i+1] - vcuts[i])
    return max_height * max_width % (10**9 + 7)
            
        