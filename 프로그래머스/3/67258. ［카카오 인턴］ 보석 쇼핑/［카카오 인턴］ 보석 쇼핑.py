def solution(gems):
    if len(gems) == 1: return [1,1]
    l = len(set(gems))
    dic = {gems[0]:1} #길이가 l일때만 답 업데이트
    answer = [1,len(gems)] #+1해준 인덱스임
    min_ans = len(gems) -1 #보다 작아야 답 업데이트
    s,e = 0,0
    while True:
        if len(dic) < l:
            e += 1
            if e == len(gems): break
            cur = gems[e]
            if cur in dic:
                dic[cur] += 1
            else:
                dic[cur] = 1
            
        else:
            if min_ans > e-s:
                answer = [s+1,e+1]
                min_ans = e-s
            cur = gems[s]
            if dic[cur] == 1:
                del dic[cur]
            else:
                dic[cur] -= 1
            s+= 1
            
            
            
    return answer