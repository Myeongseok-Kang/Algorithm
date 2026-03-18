class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mn = prices[0]
        for p in prices[1:]:
            ans = max(ans,p-mn)
            mn = min(mn,p)
        return ans