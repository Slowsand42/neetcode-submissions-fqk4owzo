class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n
        
        for i in range(n):
            xorr ^= i ^ nums[i]

        return xorr        
        
        
        
        
        # math
        
        # sum1 = 0
        
        # for i in range(len(nums) + 1):
        #     sum1 += i
        
        # return sum1 - sum(nums)