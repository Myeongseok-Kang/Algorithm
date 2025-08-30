def solution(word):
    ch = [781,156,31,6,1]
    dic = {'E':1,'I':2,'O':3,'U':4,'X':0}
    while len(word) != 5:
        word += ('X')
    val = 0
    for i,c in enumerate(word):
        if c == 'A':
            val += 1
        elif c != 'X':
            val += (dic[c]*ch[i])
            val += 1
        
            
    return val