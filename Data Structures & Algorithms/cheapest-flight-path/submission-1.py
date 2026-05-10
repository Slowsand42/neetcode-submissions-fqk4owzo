class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights: # src, dst, price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        
        return -1 if prices[dst] == float("inf") else prices[dst]
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
        # dijkstras algo (not as efficent b/c of k)

        # adj = collections.defaultdict(list)
        # for u, v, t in flights:
        #     adj[u].append((v, t))

        # minHeap = [(0, -1, src)] # price, stops, airport
        
        # while minHeap:
        #     price, stops, airport = heapq.heappop(minHeap)
        #     if airport == dst:
        #         return price

        #     for neiA, neiP in adj[airport]:
        #         if stops < k:
        #             heapq.heappush(minHeap, (price + neiP, stops + 1, neiA))

        # return -1