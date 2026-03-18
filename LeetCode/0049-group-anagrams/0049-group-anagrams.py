class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for i in range(len(strs)):
            strs[i] = list(strs[i])
            strs[i] = [strs[i],''.join(strs[i].copy())]
            strs[i][0].sort()
        strs.sort(key = lambda x: x[0])
        for i in range(len(strs)):
            strs[i][0] = ''.join(strs[i][0])
        ans = []
        tmp = []
        check = strs[0][0]
        for s1,s2 in strs:
            if check == s1: tmp.append(s2)
            else:
                check = s1
                ans.append(tmp)
                tmp = []
                tmp.append(s2)
        if tmp: ans.append(tmp)
        return ans