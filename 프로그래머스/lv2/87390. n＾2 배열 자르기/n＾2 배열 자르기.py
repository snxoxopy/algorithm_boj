def solution(n, left, right):
    answer = []
    tmp = 0
    for i in range(left, right + 1):
        r, c = i // n, i % n
        if r >= c:
            tmp = r + 1
            answer.append(tmp)    
        else:
            tmp = c + 1
            answer.append(tmp)
    return answer