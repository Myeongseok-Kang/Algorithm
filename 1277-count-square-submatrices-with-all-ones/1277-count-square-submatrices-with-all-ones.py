class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        r,c = len(matrix),len(matrix[0])
        n = min(r,c)
        cnt = 0
        for size in range(1,n+1):
            for y in range(r+1-size):
                for x in range(c+1-size):
                    flag = True
                    for i in range(y,y+size):
                        for j in range(x,x+size):
                            if matrix[i][j] == 0:
                                flag = False
                                break
                        if not flag: break
                    if flag: cnt += 1
        return cnt