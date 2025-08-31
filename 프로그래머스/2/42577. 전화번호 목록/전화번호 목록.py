def solution(phone_book):
    A = set()
    phone_book.sort(key = lambda x: len(x))
    for p in phone_book:
        tmp = ''
        for c in p[:-1]:
            tmp += c
            if tmp in A: return False
        A.add(p)
        
    return True