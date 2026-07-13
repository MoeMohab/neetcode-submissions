class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1
        mContainer = float("-inf")
        while l < r:
            cur = (r - l) * min(heights[l], heights[r])
            mContainer = max(cur, mContainer)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1 

        return mContainer
