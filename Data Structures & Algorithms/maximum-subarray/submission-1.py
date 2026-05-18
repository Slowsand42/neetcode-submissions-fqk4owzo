class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        curMax = float("-inf")

        for n in nums:
            curMax = max(n + curMax, n)
            res = max(res, curMax)
        
        return res