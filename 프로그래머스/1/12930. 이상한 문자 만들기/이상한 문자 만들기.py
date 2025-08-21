def solution(s):
    answer = ''
    cnt = 0
    for i,v in enumerate(s):
        if v == ' ':
            cnt = 0
            answer += ' '
        else:
            cnt += 1
            if cnt %2 == 1:
                answer += v.upper()
            else:
                answer += v.lower()
        
    return answer