from collections import deque
dy = [0,1]
dx = [1,0]

def solution(m, n, puddles):
    B = [[0] * m for _ in range(n)]
    B[0][0] = 1
    
    for x,y in puddles:
        B[y-1][x-1] = -1
    
    q = deque()
    q.append((0,0)) #y,x
    while q:
        cury,curx = q.popleft()
        for i in range(2):
            ny,nx = cury + dy[i] , curx +dx[i]
            if 0<=ny<=n-1 and 0<=nx<=m-1 and B[ny][nx] != -1  :
                if (ny,nx) not in q: q.append((ny,nx))
                B[ny][nx] += B[cury][curx]
                B[ny][nx] %= 1000000007
    
                    
    return B[-1][-1]
"""
결과 나누기 주의
"""