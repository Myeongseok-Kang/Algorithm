class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dy,dx = (0,0,1,-1),(1,-1,0,0)
        row,col = len(grid),len(grid[0])
        ans = 0
        for y in range(row):
            for x in range(col):
                if grid[y][x] == '1':
                    grid[y][x] = '0'
                    ans += 1
                    q = deque()
                    q.append((y,x))
                    while q:
                        cy,cx = q.popleft()
                        for d in range(4):
                            ny,nx = cy+dy[d],cx+dx[d]
                            if not 0<=ny<=row-1 or not 0<=nx<=col-1 or grid[ny][nx] == '0': continue
                            grid[ny][nx] = '0'
                            q.append((ny,nx))

        return ans

                    
