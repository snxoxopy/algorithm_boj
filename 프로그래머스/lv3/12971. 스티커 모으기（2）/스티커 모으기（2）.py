def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    answer = 0
    
    dp = [0] * len(sticker)
    
    dp[0] = sticker[0]
    dp[1] = sticker[0]
    for i in range(2, len(sticker) - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])
    answer = max(dp)
    
    dp = [0] * len(sticker)
    dp[0] = 0
    dp[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])
        
    answer = max(max(dp), answer)
    
    return answer