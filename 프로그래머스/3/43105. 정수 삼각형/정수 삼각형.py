def solution(triangle):
    answer = 0
    n = len(triangle)
    for i in range(1,n):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j],triangle[i-1][j-1])
    return max(triangle[n-1])

"""
0->0,1
1->1,2

"""