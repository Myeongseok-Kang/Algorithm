class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        dic = {}
        ans,l = 0,0 
        start = 0
        for i,c in enumerate(s):
            if c not in dic:
                l += 1
                dic[c] = i
            else:
                start = max(start,dic[c]+1)
                l = i-start + 1
                dic[c] = i
            ans = max(ans,l)
            
        return ans