from collections import deque

def solution(numbers, target):
    answer = 0
    n = 2 ** len(numbers)
    op = [0 for _ in range(len(numbers))]
    
    # 경우의 수 만들기
    # 0 = +, 1 = -
    # DEC -> BIN
    for dec in range(n):
        # print(dec, bin(dec))
        s_num = bin(dec)[2:]
        # print(s_num)
        diff = len(numbers) - len(s_num) + 1
        
        # zero-padding
        if diff > 0:
            tmp = [0 for _ in range(diff - 1)]
            for c in s_num:
                # print(c)
                tmp.append(int(c))
            # print(tmp)
    
        # 완전 탐색
        buff = 0
        for i in range(len(tmp)):
            if tmp[i] == 0: buff += numbers[i]
            else: buff -= numbers[i]
        if buff == target: answer += 1
        

    return answer