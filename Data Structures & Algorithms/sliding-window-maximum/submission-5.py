from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        l = 0
        q = deque([])
        res = []
        for r in range(n):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if r - l + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res