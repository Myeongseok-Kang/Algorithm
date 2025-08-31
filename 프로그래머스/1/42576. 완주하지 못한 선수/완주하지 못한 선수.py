def solution(participant, completion):
    dic = dict()
    for p in participant:
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1
    for c in completion:
        if dic[c] > 1:
            dic[c] -= 1
        else:
            del dic[c]
    
    
    answer = ''
    for key in dic:
        answer = key
    
    
    return answer