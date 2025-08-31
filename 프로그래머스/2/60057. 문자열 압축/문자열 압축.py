def solution(s):
    answer = len(s)
    for i in range(1,len(s)+1):
        cnt = 0 #누적 반복 횟수
        prev = '' #이전 단어
        ans = len(s)
        for j in range(0,len(s),i):# 0~7
            cur = s[j:j+i]
            if cur == prev:
                cnt += 1
                ans -= i
            else:
                if cnt != 0:
                    ans += len(str(cnt+1))
                    cnt = 0
            
            prev = s[j:j+i]
            
        if cnt != 0:
            ans += len(str(cnt+1))
            
        answer = min(ans,answer)
    return answer