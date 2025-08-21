def solution(s, n):
    answer = ''
    """
    a 97
    z 122
    
    A 65
    Z 90
    
    s에서 하나씩 뽑아서 각각 계산
    ord값이 97 ~ 122 일때
    val에 ord저장
    val값 n만큼 중가
    val <= 122면 그대로 chr바꿔 추가
    아니면 -25 하고 chr바꿔 추가
    
    ord값이 65~90일때
    나머지 다 그대로 하는데 122대신 90으로
    
    둘다 아니면
    그대로 추가
    """
    
    for c in s:
        if 97 <= ord(c) <= 122:
            val = ord(c)
            val += n
            if val <= 122: answer += chr(val)
            else: answer += chr(val-26)
        elif 65 <= ord(c) <= 90:
            val = ord(c)
            val += n
            if val <= 90: answer += chr(val)
            else: answer += chr(val-26)
        else:
            answer += c
    return answer