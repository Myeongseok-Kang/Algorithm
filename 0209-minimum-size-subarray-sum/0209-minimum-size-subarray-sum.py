class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mn_len = float("inf")
        tot = nums[0]
        s,e = 0,0
        l = 1
        while True:
            print("s = ",s,"e = ",e,"l = ",l,"tot = ",tot)
            if tot < target:
                e += 1
                if e == len(nums): break
                tot += nums[e]
                l += 1
            else:
                mn_len = min(mn_len,l)
                tot -= nums[s]
                s += 1
                l -= 1
        return mn_len if mn_len != float("inf") else 0
                

            