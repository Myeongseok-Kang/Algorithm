class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dy,dx = 0,1
        cy,cx,cnt,ans = 0,0,1,[matrix[0][0]]
        matrix[0][0] = '.'
        r,c = len(matrix),len(matrix[0])
        while True:
            ny,nx = cy+dy,cx+dx
            if not 0 <= ny < r or not 0 <= nx < c or matrix[ny][nx] == '.':
                dy,dx = dx,-dy
            else:
                cy,cx = ny,nx
                ans.append(matrix[cy][cx])
                matrix[cy][cx] = '.'
                cnt += 1
            if cnt == r*c: break
        return ans