from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_s1 = Counter(s1)
        count_s2 = defaultdict(int)
        
        t = len(count_s1)
        cur = l = r = 0

        for r in range(len(s2)):
            count_s2[s2[r]] += 1
            if s2[r] in count_s1 and count_s2[s2[r]] == count_s1[s2[r]]:
                cur += 1
            if r - l + 1 > len(s1):
                if s2[l] in count_s1 and count_s2[s2[l]] == count_s1[s2[l]]:
                    cur -= 1
                count_s2[s2[l]] -= 1
                l += 1 

            if r - l + 1 == len(s1) and cur == t:
                return True

        return False





        
        