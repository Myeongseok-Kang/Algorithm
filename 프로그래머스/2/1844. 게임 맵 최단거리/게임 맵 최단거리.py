from collections import deque

def bfs(m):
    ly,lx = len(m),len(m[0])
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    q = deque()
    q.append((0,0,1))
    visit = [[False for _ in range(lx)] for _ in range(ly)]
    visit[0][0] = True
    while q:
        cury,curx,curd = q.popleft()
        for angle in range(4):
            ny,nx,nd = cury + dy[angle] , curx + dx[angle],curd+1
            if 0<=ny<=ly-1 and 0<=nx<=lx-1 and m[ny][nx] == 1 and not visit[ny][nx]:
                if ny == ly-1 and nx == lx-1: return nd
                visit[ny][nx] = True
                q.append((ny,nx,nd))        
    return -1

def solution(maps):
    return bfs(maps)