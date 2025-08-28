def solution(sequence, k):
    answer = []
    ans_list = []
    s,e = 0,0
    summ = sequence[0]
    
    while True:
        if summ < k:
            e += 1
            if e == len(sequence): break
            summ += sequence[e]
        elif summ > k:
            summ -= sequence[s]
            s += 1
        else:
            ans_list.append([s,e])
            summ -= sequence[s]
            s += 1
    
    ans_list.sort(key = lambda x: (x[1]-x[0],x[0]))
    return ans_list[0]