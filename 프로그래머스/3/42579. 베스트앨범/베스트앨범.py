from collections import defaultdict
def solution(genres, plays):
    answer = []
    cnt = defaultdict(int)
    l = len(plays)
    for i in range(l):
        cnt[genres[i]] += plays[i]
    
    gen = [] #(장르이름,재생수)
    for key in cnt:
        gen.append((key,cnt[key]))
    gen.sort(key = lambda x: -x[1])
    gen = [x[0] for x in gen]
    
    dic = {}
    for g in gen:
        dic[g] = []
    
    for i in range(l):
        dic[genres[i]].append((plays[i],i))
    
    for g in gen:
        A = dic[g].copy()
        A.sort(key = lambda x: (-x[0],x[1]))
        A = A[:2]
        for i,j in A:
            answer.append(j)
    return answer
"""
장르당 곡 하나면 하나만

gen = 가장 많이 수록된 장르 순으로 정렬
dic = {장르:[  (재생수,곡인덱스) 가 들어가있는 배열  ]}
for g in gen:
    dic[g]의 배열을 copy 하고 정렬(기준 주의)해서 가장 많은거 1개 또는 2개
"""