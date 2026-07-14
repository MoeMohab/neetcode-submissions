from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        
        count_s1 = Counter(s1)
        count_s2 = defaultdict(int)
        cur = 0
        t = len(count_s1)
        l, r = 0, 0

        while r < m:
            count_s2[s2[r]] += 1
            if s2[r] in count_s1 and count_s2[s2[r]] == count_s1[s2[r]]:
                cur += 1
            if r - l + 1 > n:
                if s2[l] in count_s1 and count_s2[s2[l]] == count_s1[s2[l]]:
                    cur -= 1
                count_s2[s2[l]] -= 1
                l += 1 

            if r - l + 1 == n and cur == t:
                return True
            r += 1

        return False





        
        