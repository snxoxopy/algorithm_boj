def solution(m, n, puddles):
    answer = 0
    dp = [[0] * m for _ in range(n)]
    # for [c, r] in puddles:
        # dp[r - 1][c - 1] = 0
    dp[0][0] = 1
    # print(dp)
    for r in range(n):
        for c in range(m):
            if r == 0 and c == 0: continue
            if [c+1, r+1] in puddles:
                dp[r][c] = 0
            else:
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        # print(dp)
    print(dp)
    answer = dp[n-1][m-1] % 1000000007
    
    return answer