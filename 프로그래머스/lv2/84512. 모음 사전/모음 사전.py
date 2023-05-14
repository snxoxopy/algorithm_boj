def solution(word):
    answer = []
    alp = ['A', 'E', 'I', 'O', 'U']
    lst = list()
    num = 0
    
    def dfs(s):
        nonlocal lst, num
        num += 1
        if len(lst) < 5:
            for i in range(5):
                lst.append(alp[i])
                cnt = 0
                if len(word) == len(lst):
                    for j in range(len(word)):
                        if lst[j] == word[j]:
                            cnt += 1
                        if cnt == len(word):
                            # print(lst, num)
                            answer.append(num)
                            return num
                    
                dfs(alp[i])
                lst.pop()

            
    dfs(alp[0])
    return answer[0]
    
    # return answer