def solution(n):
    dy,dx = (1,0,-1),(0,1,-1)
    dd = 0
    y,x = -1,0
    tmp = 1
    ar = []
    for i in range(1,n+1):
        ar.append([0 for _ in range(i)])
    for i in range(n,0,-1):
        for _ in range(i):
            y,x = y+dy[dd],x+dx[dd]
            ar[y][x] = tmp
            tmp += 1
        dd = (dd+1) % 3
    answer = []
    for a in ar:
        for n in a:
            answer.append(n)
        
    
    
    """
    n=4
    4 3 2 1
    n = 5
    5 4 3 2 1
    
    방향은 (+1,0)  (0,+1)  (-1,-1)   반복
    처음 좌표를 (-1,0) 으로 ?
    
    
    예외: n이 1 또는 2
    """
    return answer