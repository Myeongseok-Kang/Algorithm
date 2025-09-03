from collections import deque

def solution(n, edge):
    V = [0] * n
    Elist = [[] for _ in range(n)]
    for e,s in edge:
        Elist[e-1].append(s-1)
        Elist[s-1].append(e-1)
    
    V[0] = 0
    q = deque()
    q.append(0)
    while q:
        cur = q.popleft()
        for n in Elist[cur]:
            if not V[n] and n != 0:
                V[n] = V[cur] + 1
                q.append(n)
    max_val = max(V)
    ans = V.count(max_val)
    
    """
    0번 노드로부터 가장 멀리 떨어진 노드 개수
    V가 0이면 시작이거나 아직 방문 안함 V에 거리 저장함
    """
    return ans