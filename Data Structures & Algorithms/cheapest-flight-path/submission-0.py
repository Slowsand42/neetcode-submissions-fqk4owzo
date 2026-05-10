class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, t in flights:
            adj[u].append((v, t))

        minHeap = [(0, -1, src)] # price, stops, airport
        
        while minHeap:
            price, stops, airport = heapq.heappop(minHeap)
            if airport == dst:
                return price

            for neiA, neiP in adj[airport]:
                if stops < k:
                    heapq.heappush(minHeap, (price + neiP, stops + 1, neiA))

        return -1