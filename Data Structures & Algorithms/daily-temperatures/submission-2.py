class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []

        for i in range(len(temperatures)):
            while s and temperatures[s[-1]] < temperatures[i]:
                idx = s.pop()
                res[idx] = i - idx    
            s.append(i)
        return res

        