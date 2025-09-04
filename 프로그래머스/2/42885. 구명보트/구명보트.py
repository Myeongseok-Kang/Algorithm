def solution(people, limit):
    if len(people) == 1:
        return 1
    
    people.sort()
    s,e = 0,len(people)-1
    
    answer = len(people) #두명 탈때마다 1씩 감소
    
    while True: # s!=e
        if people[s] + people[e] > limit:
            e -= 1
            if s == e: break
        else:
            answer -= 1
            s += 1
            e -= 1
            if s >= e: break
    return answer
"""
50 50 70 80
"""