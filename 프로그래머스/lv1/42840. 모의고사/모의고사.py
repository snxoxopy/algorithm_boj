def extend_len(ans, sol):
    while len(ans) >= len(sol):
        sol *= 2
    return sol

def solution(answers):
    answer = []
    sol_1 = [1, 2, 3, 4, 5]
    sol_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    sol_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt_1, cnt_2, cnt_3 = 0, 0, 0
    

    extend_len(answers, sol_1)
    extend_len(answers, sol_2)
    extend_len(answers, sol_3)
    
    # print(sol_1, sol_2, sol_3)
    
    for i in range(len(answers)):
        if answers[i] == sol_1[i]:
            cnt_1 += 1
        if answers[i] == sol_2[i]:
            cnt_2 += 1
        if answers[i] == sol_3[i]:
            cnt_3 += 1
    
    max_sol = [cnt_1, cnt_2, cnt_3]
    # print(max_sol)
    
    max_cnt = max(max_sol)
    for i in range(3):
        if max_sol[i] == max_cnt:
            answer.append(i + 1)
    
    return answer