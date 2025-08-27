def solution(n):
    dy = [1,0,-1]
    dx = [0,1,-1]
    B = [[0] * n for _ in range(n)]
    cy,cx = -1,0
    angle = 0
    num = 1
    for i in range(n,0,-1): #4 3 2 1
        for _ in range(i):
            ny,nx = cy+dy[angle],cx+dx[angle]
            B[ny][nx] = num
            num += 1
            cy,cx = ny,nx
        angle = (angle +1)%3
    answer = []
    
    for b in B:
        for a in b:
            if a != 0: answer.append(a)
    return answer