from collections import deque
dy = [-1,1,0,0]
dx = [0,0,-1,1]


def bfs(place):
    for y in range(5):
        for x in range(5):
            if place[y][x] == 'P':
                q = deque()
                q.append((y,x,0))
                visit = [[False] * 5 for _ in range(5)]
                visit[y][x] = True
                while q:    
                    cury,curx,curd = q.popleft()
                    if curd == 2: continue
                    for angle in range(4):
                        ny,nx,nd = cury+dy[angle],curx+dx[angle],curd+1
                        if (0<=ny<=4 and 0<=nx<=4 and not visit[ny][nx] and place[ny][nx] != 'X'):
                            if place[ny][nx] == 'P': return 0
                            visit[ny][nx] = True
                            q.append((ny,nx,nd))
    return 1
        
def solution(places):
    
    answer = []

    for p in places:
        answer.append(bfs(p))
    return answer