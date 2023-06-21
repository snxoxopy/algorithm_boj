def solution(elements):
    answer = 0
    # lst = []
    res = set()
    len_e = len(elements) * 2
    copy_e = elements * 2
    # print(copy_e)
    lst = set()
    for width in range(1, len_e//2 + 1):
        for i in range(len_e//2):
            # print(copy_e[i:i+width])
            res.add(sum(copy_e[i:i+width]))
            # print(res)
    
            
#     def dfs(num, dep, visited):
#         # end
#         nonlocal lst
#         if len(lst) == dep:
#             res.add(sum(lst))
#             print(lst)
#             return
#         else:
#             for j in range(len(elements)):
#                 if not visited[j]:
#                     visited[j] = 1
#                     lst.append(elements[j])
#                     dfs(elements[j], dep, visited)
#                     lst.pop()
#                     visited[j] = 0                    
    
#     for i in range(1, len(elements) + 1):
#         lst = []
#         visited = [0 for _ in range(len(elements))]
#         for j in range(len(elements)):
#             e = elements[j]
#             visited[j] = 1
#             lst.append(e)
#             dfs(e, i, visited)
#             lst.pop()
            
    # print(res)
    answer = len(res)
    return answer