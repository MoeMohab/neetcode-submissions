class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        s = []
        res = []
        counter = 0
        for i in range(len(temperatures)):
            flag = False
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    res.append(j - i)
                    flag = True
                    break
            if not flag:
                res.append(0)
        return res
        