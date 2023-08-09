n = int(input())
lst = list()
lst_num = [1, 2, 3]
flag_exit = 0


def chk_continuity(res):
    for width in range(1, len(res)//2 + 1):
        if res[-2 * width : -1 * width] == res[-1 * width : ]:
            return False
    return True


def dfs():
    global lst, flag_exit
    if flag_exit == 1:
        return
    if len(lst) == n:
        answer = str()
        for s in lst:
            answer += str(s)
        print(answer)
        flag_exit = 1
    for i in range(3):
        lst.append(lst_num[i])
        if chk_continuity(lst):
            dfs()
        lst.pop()

dfs()