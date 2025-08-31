from itertools import permutations

def solution(expression):
    answer = 0
    nums = []
    op = []
    ptr = 0
    for i in range(len(expression)):
        if not expression[i].isdigit():
            nums.append(int(expression[ptr:i]))
            op.append(expression[i])
            ptr = i + 1
    nums.append(int(expression[ptr:]))
    
    A = set()
    for c in expression:
        if not c.isdigit():
            A.add(c)
    A = list(A)
    
    if len(nums) == 1: return nums[0]
    for per in permutations(A,len(A)): #per은 연산자 우선순위
        nn = nums.copy()
        oo = op.copy()
        
        for p in per:
            while p in oo:
                idx = oo.index(p)
                if p == '-':
                    val = nn.pop(idx) - nn.pop(idx)
                elif p == '+':
                    val = nn.pop(idx) + nn.pop(idx)
                else:
                    val = nn.pop(idx) * nn.pop(idx)
                nn.insert(idx,val)
                oo.pop(idx)
        answer = max(abs(nn[0]),answer)
            
    return answer