def solution(s):
    answer = 0
    len_s = len(s)
    dp = [[0] * len_s for _ in range(len_s)]

    for start in range(len_s):
        dp[start][start] = 1
        answer = 1
        end = start + 1
        if end == len_s: break
        if s[start] == s[end]:
            dp[start][end] = 1


    for scan in range(2, len_s):
        for start in range(len_s):
            end = start + scan
            if end == len_s: break
            if (s[start] == s[end] and dp[start + 1][end - 1]):
                dp[start][end] = 1
                answer = scan + 1

    return answer