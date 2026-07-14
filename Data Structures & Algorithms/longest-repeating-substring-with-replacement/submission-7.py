from collections import defaultdict, Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        count = defaultdict(int)
        l, r = 0, 0
        ch = ''
        maxf = 0
        res = 0
        while r < n:
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
            r += 1
        
        return res



        