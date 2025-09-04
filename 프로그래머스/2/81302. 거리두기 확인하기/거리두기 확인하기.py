from collections import deque
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def solution(places):
    
    answer = []
    for place in places:
        ans = 1
        people = []
        for y in range(5):
            for x in range(5):
                if place[y][x] == 'P': people.append((y,x))
        
        for y,x in people:
            q = deque()
            q.append((y,x,0))
            while q:
                cury,curx,curd = q.popleft()
                for i in range(4):
                    ny,nx = cury+dy[i],curx+dx[i]
                    if 0<=ny<=4 and 0<=nx<=4 and place[ny][nx] != 'X' and curd <= 1:
                        if place[ny][nx] == 'P' and not (ny == y and nx == x): ans = 0
                        else: q.append((ny,nx,curd+1))
        answer.append(ans)

    return answer