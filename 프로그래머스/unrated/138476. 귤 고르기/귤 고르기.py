def solution(k, tangerine):
    answer = 0
    lst = dict()
    
    for w in tangerine:
        lst[w] = 0
    
    for w in tangerine:
        lst[w] += 1
    
    lst = sorted(lst.items(), key = lambda x : -x[1])
    # print(lst)
    
    pick = 0
    basket = []

    for size, cnt in lst:
        if pick < k:
            pick += cnt
            basket.append(size)
        

    # print(basket)
    answer = len(basket)
    
    return answer