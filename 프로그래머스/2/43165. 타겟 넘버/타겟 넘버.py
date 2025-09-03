from collections import deque

def solution(numbers, target):
    q = deque()
    q.append((0,0))
    ans = 0
    while q:
        cur,idx = q.popleft()
        for i in range(2):
            if i == 0:
                n = cur + numbers[idx]
            elif i == 1:
                n = cur - numbers[idx]
                
            if idx == len(numbers)-1:
                if n == target: ans += 1
            else:
                q.append((n,idx+1))
    return ans
                
        