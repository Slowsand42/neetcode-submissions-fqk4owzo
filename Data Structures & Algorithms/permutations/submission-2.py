class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(arr1, arr2):
            if len(arr1) == len(nums):
                res.append(arr1.copy())
                return
            
            for i in range(len(arr2)):
                arr1.append(arr2[i])
                dfs(arr1, arr2[:i] + arr2[i + 1:])
                arr1.pop()
        
        dfs([], nums)
        return res