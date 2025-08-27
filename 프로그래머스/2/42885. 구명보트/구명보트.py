def solution(people, limit):
    s = 0
    e = len(people) -1
    answer = 0
    people.sort()
    while s<=e: 
        if people[e] + people[s] > limit:
            answer += 1
            e -= 1
        else:
            e -= 1
            s += 1
            answer += 1
        if s == e:
            answer += 1
            e-=1
            s+= 1
    return answer