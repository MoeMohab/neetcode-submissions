class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        mL, mR = height[0], height[r]
        res = 0
        while l < r:
            if mL < mR:
                l += 1
                mL = max(mL, height[l])
                res += mL - height[l]
            else:
                r -= 1
                mR = max(mR, height[r])
                res += mR - height[r]
        
        return res