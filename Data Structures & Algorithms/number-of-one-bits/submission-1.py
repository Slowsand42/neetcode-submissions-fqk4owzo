class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        
        while n:
            n = n & (n - 1)
            res += 1
        
        return res
        
        
        
        
        # using & O(32)
        
        # res = 0

        # while n:
        #     res += n & 1
        #     n = n >> 1
        
        # return res