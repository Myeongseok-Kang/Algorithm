class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        dd = 0
        cury,curx = 0,0
        ny,nx = 0,0
        cnt = 1
        m,n = len(matrix),len(matrix[0])
        ans = []
        ans.append(matrix[0][0])
        visit = [[0 for _ in range(n)] for _ in range(m)]
        visit[0][0] = 1 
        while True:
            ny,nx = cury+dir[dd][0] , curx + dir[dd][1]
            if cnt == m*n: break
            if 0 <= ny <= m-1 and 0 <= nx <= n-1 and not visit[ny][nx]:
                visit[ny][nx] = 1
                cury,curx = ny,nx
                cnt += 1
                ans.append(matrix[ny][nx])
            else:
                dd = (dd+1)%4
                
        return ans
