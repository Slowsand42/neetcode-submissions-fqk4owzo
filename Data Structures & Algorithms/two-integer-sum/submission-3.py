class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i, n in enumerate(nums):
            dif = target - n
            if dif in numMap:
                return [numMap[dif], i]
            numMap[n] = i