def solution(rows, columns, queries):
    answer = []
    cols = columns
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    tmp = 0
    for y in range(rows):
        for x in range(cols):
            tmp += 1
            board[y][x] = tmp
    
    for r1,c1,r2,c2 in queries:
        r1,c1,r2,c2 = r1-1,c1-1,r2-1,c2-1
        val = []
        for x in range(c1,c2+1):
            val.append(board[r1][x])
        for y in range(r1+1,r2+1):
            val.append(board[y][c2])
        for x in range(c2-1,c1-1,-1):
            val.append(board[r2][x])
        for y in range(r2-1,r1,-1):
            val.append(board[y][c1])
        val.insert(0,val[-1])
        val = val[:-1]
        
        idx = 0
        for x in range(c1,c2+1):
            board[r1][x] = val[idx]
            idx += 1
        for y in range(r1+1,r2+1):
            board[y][c2] = val[idx]
            idx += 1
        for x in range(c2-1,c1-1,-1):
            board[r2][x] = val[idx]
            idx += 1
        for y in range(r2-1,r1,-1):
            board[y][c1] = val[idx]
            idx += 1
        answer.append(min(val))
        
    
    return answer