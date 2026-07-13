class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1
        mContainer = float("-inf")
        while l < r:
            mContainer = max(((r - l) * min(heights[l], heights[r])), mContainer)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return mContainer
