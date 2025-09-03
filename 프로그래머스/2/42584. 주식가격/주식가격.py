def solution(prices):
    l = len(prices)
    answer = [0] * l
    stack = []
    for t in range(l):
        if not stack or prices[stack[-1]] <= prices[t]:
            stack.append(t)
        else:
            while (stack and prices[stack[-1]] > prices[t]):
                idx = stack.pop()
                answer[idx] = t-idx
            stack.append(t)
    t = l-1
    while stack:
        idx = stack.pop()
        answer[idx] = t-idx
    
    return answer