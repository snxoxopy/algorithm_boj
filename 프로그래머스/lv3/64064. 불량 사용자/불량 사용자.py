def solution(user_id, banned_id):
    answer = 0
    len_u, len_b = len(user_id), len(banned_id)
    
    # DFS
    lst = []
    
    def masking(uid):
        cnt = 0
        visited = [0] * len_b
        for i in range(len(uid)):
            str_user = uid[i]
            flag = 0
            for j in range(len_b):
                str_ban = banned_id[j]
                if len(str_user) == len(str_ban):
                    flag = 1
                    for k in range(len(str_ban)):
                        if str_ban[k] != '*' and str_ban[k] != str_user[k]:
                            flag = 0
                            break
                    if flag and not visited[j]:
                        visited[j] = 1
                        cnt += 1
                        break
                else: continue

        return cnt
            
    set_answer = set()
    def dfs(depth):
        if len(lst) == len_b:
            if masking(lst) == len_b:
                ver = sorted(lst)
                set_answer.add(tuple(ver))
                return set_answer
        else:
            for i in range(len_u):
                if user_id[i] not in lst:
                    lst.append(user_id[i])
                    dfs(depth + 1)
                    lst.pop()
    # main
    dfs(0)
    
    answer = len(set_answer)
    return answer