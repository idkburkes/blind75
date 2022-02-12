from heapq import heappush, heappop

def connectSticks(self, sticks: List[int]) -> int:
    if not sticks or len(sticks) <= 1:
        return 0
    res, heap = 0, []
    for stick in sticks:
        heappush(heap, stick) 
    while len(heap) > 1:
        stick1, stick2 = heappop(heap), heappop(heap)
        res += stick1 + stick2
        heappush(heap, stick1 + stick2)
    return res