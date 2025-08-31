from itertools import permutations

def match(s1,s2): #2번이 *들어감
    if len(s1) != len(s2): return False
    for i in range(len(s1)):
        if s2[i] != '*' and s2[i] != s1[i]: return False
    return True

def solution(user_id, banned_id):
    memory = set()
    for i in permutations(user_id,len(banned_id)):
        i = list(i)
        flag = True
        for j in range(len(i)):
            if not match(i[j],banned_id[j]): flag = False
            
        if flag == True:
            k = sorted(i)
            tmp = ''
            for id in k:
                tmp += id
                tmp += ','
            memory.add(tmp)
    
    return len(memory)