class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ar = [0] * len(nums) 
        ar[0] = nums[0]
        for i in range(1,len(nums)):
            ar[i] = ar[i-1] + nums[i] if ar[i-1] > 0 else nums[i]
        return max(ar)