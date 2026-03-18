from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
        ar = []
        for v in dic.keys():
            w = dic[v]
            ar.append((v,w))
        ar.sort(key = lambda x: -x[1])
        ans = [x[0] for x in ar[:k]]
        return ans