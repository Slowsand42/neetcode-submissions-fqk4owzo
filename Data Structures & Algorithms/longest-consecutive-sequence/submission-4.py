class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in nums:
            length = 0

            if n - 1 in numSet:
                continue

            while n + length in numSet:
                length += 1
                res = max(res, length)
            
        return res