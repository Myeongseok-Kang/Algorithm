class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        e = k-1
        mn,tot = sum(nums[s:e+1]),sum(nums[s:e+1])
        while True:
            if e+1 == len(nums): break
            tot -= nums[s]
            tot += nums[e+1]
            s,e = s+1,e+1
            mn = max(mn,tot)
            
        return mn/k
            
