class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: (x[0],x[1]))
        print(intervals)
        s,e = intervals[0]
        ans = []
        for ns,ne in intervals[1:]:
            if e>=ns: e = max(e,ne)
            else:
                ans.append([s,e])
                s,e = ns,ne
        ans.append([s,e])
        return ans

        