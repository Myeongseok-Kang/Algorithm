def solution(n, times):
    s,e = 1,max(times)*n
    while s<=e:
        m = (s+e)//2
        total = 0
        for t in times:
            total += (m//t)
        
        if total < n: #m시간에 n명처리 안된다
            s = m+1
        else: #된다
            answer = m
            e = m-1
    
    return answer