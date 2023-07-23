
def solution(sequence):
    min_e1, min_e2 = 0, 0
    answer = -100001
    e1, e2 = 0, 0
    flag = 1
    
    for e in sequence:
        e1 += e * flag
        e2 += e * -1 * flag
        
        answer = max(answer, e1 - min_e1, e2 - min_e2)
        
        min_e1 = min(e1, min_e1)
        min_e2 = min(e2, min_e2)
        
        flag *= -1
        
    return answer