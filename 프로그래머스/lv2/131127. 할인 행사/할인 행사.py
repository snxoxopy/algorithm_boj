def solution(want, number, discount):
    answer = 0
    lst = dict()
    
    for pr in discount:
        lst[pr] = 0

    for day in range(len(discount) - 9):
        for i in range(day, day + 10):
             lst[discount[i]] += 1
        cnt = 0
        # print(lst)
        for product, num in zip(want, number):
            if product in lst and lst[product] >= num:
                cnt += 1
                # print(cnt)
        if cnt == len(want):
            answer += 1
            # print(day, cnt)
            
        for item in lst:
            lst[item] = 0

        
    return answer