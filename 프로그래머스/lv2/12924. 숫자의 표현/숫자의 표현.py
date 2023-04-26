def solution(n):
    answer = 0
    
    # q = n // 2
    for i in range(1, n + 1):
        i_sum = 0
        for j in range(i, n + 1):
            i_sum += j
            # print(j)
            if i_sum == n:
                answer += 1
                break
            elif i_sum > n:
                break
    
    
    return answer