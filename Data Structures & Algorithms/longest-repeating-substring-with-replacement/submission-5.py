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
            if not ch:
                ch = s[r]
            if count[s[r]] > maxf:
                maxf = count[s[r]]
                ch = s[r]
            if (r - l + 1) - maxf <= k:
                res = max(res, r - l +1)
            else:
                count[s[l]] -= 1
                if s[l] == ch:
                    maxf -= 1
                l += 1
            r += 1
        
        return res



        