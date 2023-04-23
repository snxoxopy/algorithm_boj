def solution(n):
    answer = 0
    
    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 0, 1, 2
    
    # dp[n] = dp[n - 1] + dp[n - 2]
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2])%1000000007
    
    answer = dp[n]
    
    return answer