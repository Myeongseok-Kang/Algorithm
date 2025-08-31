from collections import defaultdict

def solution(clothes):
    dic = defaultdict(int)
    for i,j in clothes:
        dic[j] += 1
    answer = 1
    for key in dic:
        answer *= (dic[key]+1)
    return answer-1