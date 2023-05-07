def solution(n, words):
    answer = []
    lst = [words[0]]
    end = words[0][-1]
    # print(end)
    
    for i in range(1, len(words)):
        if not words[i] in lst:
            if end == words[i][0]:
                lst.append(words[i])
            else: break
        else: break
        end = words[i][-1]
    print(len(lst) % n, len(lst) // n)
    answer = [len(lst) % n + 1, len(lst) // n + 1]
    if len(lst) == len(words): answer = [0, 0]

    return answer