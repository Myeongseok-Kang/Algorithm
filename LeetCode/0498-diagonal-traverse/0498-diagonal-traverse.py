class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat) == 1 and len(mat[0]) == 1: return [mat[0][0]]
        y,x = 0,0
        dd = 0
        r = len(mat)
        c = len(mat[0])
        dy = [-1,1]
        dx = [1,-1]
        ans = [mat[0][0]]
        while True:
            ny,nx = y+dy[dd], x+dx[dd]
            if 0 <= nx < c and 0 <= ny < r:
                y,x = ny,nx
            else:
                if not 0 <= nx < c and not 0<= ny <r:
                    if dd == 0: y += 1
                    else: x += 1
                elif not 0 <= nx < c and 0<= ny <r:
                    y += 1
                elif 0 <= nx < c and not 0<= ny <r:
                    x += 1
                dd = (dd+1) % 2
            ans.append(mat[y][x])
            if y == r-1 and x == c-1: break
        return ans