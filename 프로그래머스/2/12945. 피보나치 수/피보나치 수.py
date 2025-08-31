def solution(n):
    
    A = [0] * (n+1)
    A[1] = 1
    for i in range(2,n+1):
        A[i] = (A[i-1] + A[i-2])%1234567
    return A[n]