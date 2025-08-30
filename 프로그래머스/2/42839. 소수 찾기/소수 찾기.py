from itertools import permutations

def isprime(n):
    if n == 0 or n == 1: return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0: return False
    return True

nums = set()
"""
중복불가능, 앞에0붙으면같은거
"""
def solution(numbers):
    numbers = list(numbers)
    visit = [False] * len(numbers)
    
    for i in range(1,len(numbers)+1):
        for j in permutations(numbers,i):
            nums.add(int(''.join(j)))
    ns = list(nums)
    answer = 0
    for n in ns:
        if isprime(n): answer += 1
    return answer