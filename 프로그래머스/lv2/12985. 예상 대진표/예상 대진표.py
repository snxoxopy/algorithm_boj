def solution(n, a, b):
    answer = 0
    
    while 1:
        a = (a // 2) + (a % 2)
        b = (b // 2) + (b % 2)
        if a == b: break
        answer += 1
    
    
    return answer + 1