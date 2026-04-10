class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0
        highestArea = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            highestArea = max(area, highestArea)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return highestArea

        # height[min(l or r)] * (r - l)
        # two pointers
        # whichever height is smaller, either increment or decrement l or r
        # store highest and return max