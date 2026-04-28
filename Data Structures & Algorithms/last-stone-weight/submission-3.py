class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones
        heapq.heapify_max(maxHeap)

        while len(maxHeap) > 1:
            x = heapq.heappop_max(maxHeap)
            y = heapq.heappop_max(maxHeap)

            heapq.heappush_max(maxHeap, x - y)
            
        return maxHeap[0] 