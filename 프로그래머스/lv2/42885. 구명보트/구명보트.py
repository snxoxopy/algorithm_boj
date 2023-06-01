def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    # print(people)
    ptr_l, ptr_r = 0, len(people) - 1
    
    while(ptr_r > ptr_l):
        w = people[ptr_l] + people[ptr_r]
        if w > limit:
            ptr_l += 1
        else:
            ptr_l += 1
            ptr_r -= 1
        answer += 1
    
    if ptr_l == ptr_r: answer += 1
    
    return answer