def solution(line):
    arr = []

    for i in range(len(line)):
        for j in range(i+1,len(line)):
            A,B,E = line[i]
            C,D,F = line[j]
            if (A*D)-(B*C) == 0: continue
            x = ((B*F) - (E*D))/((A*D)-(B*C))
            y = ((E*C) - (A*F))/((A*D)-(B*C))
            if x == int(x) and y == int(y):
                arr.append((y,x))
    
    min_x,min_y,max_x,max_y = float('inf'),float('inf'),-float('inf'),-float('inf')
    for x,y in arr:
        if x < min_x: min_x = x
        if y < min_y: min_y = y
        if x > max_x: max_x = x
        if y > max_y: max_y = y
    
    dy = int(max_y-min_y+1)
    dx = int(max_x-min_x+1)
    ans = [['.'] * (dy) for _ in range(dx)]
    
    for x,y in arr:
        nx = int(x-min_x)
        ny = int(y-min_y)
        ans[nx][ny] = '*'

    print(arr)
    new = []
    for an in ans:
        new.append(''.join(an))
    return new[::-1]