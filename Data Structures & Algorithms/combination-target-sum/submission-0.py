class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            # first decision to include candidate
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            # do not include the candidate (to avoid duplicates)
            curr.pop()
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return res