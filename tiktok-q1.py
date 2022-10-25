import collections

class Solution:
    def minIncrementForUnique(self, nums):
        max_val = max(nums)
        count = collections.Counter(nums)
        
        taken = 0
        ans = 0
        for n in range(len(nums) + max_val):
            if count[n] >= 2:
                taken += count[n] - 1
                ans -= n * (count[n] - 1)
            elif taken and count[n] == 0:
                ans += n
                taken -= 1
        return ans