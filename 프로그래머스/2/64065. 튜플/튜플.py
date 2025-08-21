def solution(s):
    answer = []
    """
    튜플 추출해서 정렬하고
    튜플 번호과 인덱스 1씩 증가시키면서 answer에 넣음
    
    """
    s = s[2:-2]
    tuples = s.split("},{")
    
    for i,t in enumerate(tuples):
        tuples[i] = t.split(',')
    
    tuples.sort(key = lambda x: len(x))
    
    
    for t in tuples:
        for v in t:
            if v not in answer:
                answer.append(v)
    answer = [int(x) for x in answer]
        
    return answer