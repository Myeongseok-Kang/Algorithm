def f(num,depth):
    if num == 1:
        return depth
    if depth == 500 and num != 1: return -1
    if num % 2 == 0:
        return f(num//2,depth+1)
    else:
        return f(num*3+1,depth+1)

def solution(num):
    return f(num,0)