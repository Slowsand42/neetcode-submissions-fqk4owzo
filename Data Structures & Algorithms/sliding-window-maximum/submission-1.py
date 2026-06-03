class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        res = []
        curMax = -10000

        while r < len(nums):
            for i in range(l, r + 1):
                curMax = max(curMax, nums[i])
            res.append(curMax)
            curMax = -10000
            l += 1
            r += 1
        
        return res