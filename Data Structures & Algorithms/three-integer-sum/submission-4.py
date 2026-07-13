class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSums(arr, target):
            n = len(arr)-1
            l, r = 0, n
            ret = []
            while l < r:
                cur = arr[l] + arr[r]
                if cur == target:
                    ret.append([arr[l], arr[r]])
                    l += 1
                    r -= 1
                    while l < r and arr[l] == arr[l-1]:
                        l += 1
                    while l < r and arr[r] == arr[r+1]:
                        r -= 1
                elif cur < target:
                    l += 1
                else:
                    r -= 1
            return ret
                
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            ret = twoSums(nums[i+1:], target)
            if ret:
                res = res + [r + [nums[i]] for r in ret]
                
        return res
        
        
            
