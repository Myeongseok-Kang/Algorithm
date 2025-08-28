def solution(s):
    answer = [0,0]
    while s!= '1':
        answer[0] += 1
        tmp = 0
        l = len(s)
        for c in s:
            if c == '0': tmp += 1
        answer[1] += tmp
        s = bin(l-tmp)[2:]
    return answer