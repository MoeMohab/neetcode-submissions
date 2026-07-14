class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l, r = 0, 1
        p = 0

        while r < n:
            p = max(p, prices[r] - prices[l])
            if prices[r] <= prices[l]:
                l = r
                r += 1
            else:
                r += 1
        
        return p