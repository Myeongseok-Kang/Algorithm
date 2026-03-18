class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            nums[i] = [nums[i],i] 
        nums.sort(key =lambda x: x[0])
        s,e = 0,len(nums)-1
        val = nums[s][0] + nums[e][0]
        while s<e:
            if val == target:
                break
            elif val < target:
                val -= nums[s][0]
                s += 1
                val += nums[s][0]
            else:
                val -= nums[e][0]
                e -= 1
                val += nums[e][0]
        return [nums[s][1],nums[e][1]]