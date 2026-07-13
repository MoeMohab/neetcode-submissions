class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSums(arr, target):
            n = len(arr)-1
            l, r = 0, n
            ret = set()
            while l < r:
                cur = arr[l] + arr[r]
                if cur == target:
                    ret.add((arr[l], arr[r]))
                    l += 1
                    r -= 1
                elif cur < target:
                    l += 1
                else:
                    r -= 1
            return ret
                
        res = set()
        nums.sort()

        for i in range(len(nums)):
            target = 0 - nums[i]
            ret = twoSums(nums[i+1:], target)
            if ret:
                l = [res.add(tuple(list(r) + [nums[i]])) for r in ret]
                
        return [list(r) for r in res]
        
        
            
