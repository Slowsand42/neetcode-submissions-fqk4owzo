class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [s for s in stones]
        heapq.heapify_max(maxHeap)

        while len(maxHeap) > 1:
            y = heapq.heappop_max(maxHeap)
            x = heapq.heappop_max(maxHeap)

            if y > x:
                heapq.heappush_max(maxHeap, y - x)
                
        if maxHeap:
            return maxHeap[0]
        else:
            return 0