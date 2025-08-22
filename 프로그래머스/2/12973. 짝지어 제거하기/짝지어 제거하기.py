def solution(s):
    answer = -1

    """
    모두제거 1
    아니면 0
    
    for:  stack에 하나씩 순서대로 추가함
    b     baa
    """
    if len(s) == 1: return 0
    if len(s) == 2:
        if s[0] == s[1]: return 1
        else: return 0
    
    stack = []
    stack.append(s[0])
    for c in s[1:]:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    if stack: return 0
    else: return 1