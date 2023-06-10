def solution(k, dungeons):
    answer = 0
    visited = [0 for _ in range(len(dungeons))]
    lst_ans = []
    
    def dfs(dep):
        nonlocal answer
        if dep == len(dungeons):
            # print(lst_ans)
            p_cal, cnt = k, 0
            for p_min, p_con in lst_ans:
                # print(p_min, p_con)
                if p_cal >= p_min:
                    p_cal -= p_con
                    cnt += 1
                    # print(cnt)
                answer = max(cnt, answer)
            return 
        else:
            for i in range(len(dungeons)):
                if not visited[i]:
                    visited[i] = 1
                    lst_ans.append(dungeons[i])
                    dfs(dep + 1)
                    lst_ans.pop()
                    visited[i] = 0
    # main
    dfs(0)

    return answer