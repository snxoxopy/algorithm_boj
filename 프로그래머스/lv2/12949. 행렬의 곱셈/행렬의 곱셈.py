def solution(arr1, arr2):
    # size: len(arr1) x len(arr2[0])
    l_r, l_c = len(arr1), len(arr2[0])
    answer = [[0] * l_c for _ in range(l_r)]
    
    # arr1: 열증가
    # arr2: 행증가
    for k in range(l_r):
        for i in range(l_c):
            e = 0
            for j in range(len(arr1[0])):
                e = e + (arr1[k][j] * arr2[j][i])
            answer[k][i] = e
    return answer