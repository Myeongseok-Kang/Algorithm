def solution(gems):
    if len(gems) == 1: return [1, 1]
    answer = [] #+1해서 업데이트 해야함
    min_len = len(gems)+1 #amswer의
    dic = dict() #len(dic) == size일때 구간 만족, 0으로 변하면 del로 삭제 필요
    dic[gems[0]] = 1
    size = len(set(gems))
    s,e = 0,0
    while e <= len(gems)-1:
        if size == len(dic):
            if e-s+1 < min_len:
                min_len = e-s+1
                answer = [s+1,e+1]
            if dic[gems[s]] == 1: del dic[gems[s]]
            else: dic[gems[s]] -= 1
            s += 1
        else:
            e += 1
            if e>=len(gems): break
            if gems[e] in dic: dic[gems[e]] += 1
            else:
                dic[gems[e]] = 1
    
    return answer