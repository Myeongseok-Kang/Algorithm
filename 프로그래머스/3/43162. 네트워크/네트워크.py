from collections import deque

def solution(n, computers):
    answer = 0
    Elist = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] and i != j:
                Elist[i].append(j)
                Elist[j].append(i)
    
    V = [False] * n
    for i in range(n):
        if not V[i]:
            answer += 1
            q = deque()
            q.append(i)
            V[i] = True
            while q:
                cur = q.popleft()
                for nn in Elist[cur]:
                    if not V[nn]:
                        V[nn] = True
                        q.append(nn)
    
    return answer