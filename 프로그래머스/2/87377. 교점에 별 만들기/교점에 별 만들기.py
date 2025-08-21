def solution(line):
    cross = []

    
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            A,B,E = line[i]
            C,D,F = line[j]
            if A*D == B*C: continue
            cx = (B*F - E*D)/(A*D - B*C)
            cy = (E*C - A*F)/(A*D - B*C)
            if cx == int(cx) and cy == int(cy):
                cross.append([int(cx),int(cy)])
    sx,sy,ex,ey = float("inf"),float("inf"),-float("inf"),-float("inf")
    for x,y in cross:
        sx,sy = min(x,sx),min(y,sy)
        ex,ey = max(x,ex),max(y,ey)
    tx = ex-sx
    ty = ey-sy
    board = [['.' for _ in range(tx+1)] for _ in range(ty+1)]
    
    
    for x,y in cross:
        board[ey-y][x-sx] = '*'
        
    board = [''.join(row) for row in board]
    return board