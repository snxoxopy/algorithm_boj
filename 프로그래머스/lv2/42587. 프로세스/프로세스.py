from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque() # location, priorities
    os = deque()
    len_p = len(priorities)
    sort_prio = sorted(priorities, reverse = True)
    # print(sort_prio)
    for i in range(len_p):
        # os[i] = priorities[i]
        q.append([i, priorities[i]])
    # print(q)
    j = 0
    while q:
        i, prio = q.popleft()
        s_prio = sort_prio[j]
        if s_prio == prio :
            os.append([i, prio])
            j += 1
        else:
            q.append([i, prio])
            
    # print(os)
    k = 1
    for l, p in os:
        if l == location:
            answer = k
            break
        k += 1
        
    
    return answer

# def solution(priorities, location):
#     answer = 0
#     p_tmp = 0
#     p_len = len(priorities)
    
#     os = dict() # key = proccess, value = priority
    
#     for i in range(p_len):
#         os[i] = priorities[i]
    
#     s_os = sorted(os.items(), key = lambda x: x[1])
#     print(s_os) # key 거꾸로 읽으면 순서 완성
    
#     # 이 방법의 문제점: [1, 1, 9, 1, 1, 1] -> 0번째 1이 가장 첫번째 요소로 오게된다.
#     j = p_len - 1
#     for proc, prio in s_os:
#         print(j, proc, prio)
#         if location == proc:
#             answer = j + 1
#             break
#         j -= 1
        
    
#     # answer = s_os[p_len - location - 1]
    
#     return answer