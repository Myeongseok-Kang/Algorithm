def solution(answers):
    p1 = [1,2,3,4,5] # 5
    p2 = [2,1,2,3,2,4,2,5] # 8
    p3 = [3,3,1,1,2,2,4,4,5,5] # 10
    ans1,ans2,ans3 = 0,0,0
    
    for i,v in enumerate(answers):
        if v == p1[i%5]: ans1 += 1
        if v == p2[i%8]: ans2 += 1
        if v == p3[i%10]: ans3 += 1
    maxx = max(ans1,ans2,ans3)
    answer = []
    if ans1 == maxx: answer.append(1)
    if ans2 == maxx: answer.append(2)
    if ans3 == maxx: answer.append(3)
    return answer