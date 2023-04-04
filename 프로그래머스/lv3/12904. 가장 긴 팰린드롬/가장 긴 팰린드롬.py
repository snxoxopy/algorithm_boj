def solution(s):
    answer = 0
    len_s = len(s)
    # dp = [[0]*len_s]*len_s
    dp = [[0 for _ in range(len_s)] for _ in range(len_s)]
    # print(dp)
    
    for i in range(len_s):
        # print(i)
        dp[i][i] = 1
        # print(dp)
        answer = 1
    # print(dp)

    for i in range(len_s - 1):
        if(s[i] == s[i+1]):
            # print(s[i], s[i+1])
            dp[i][i+1] = 1

    # print(dp)
    
    for width in range(3, len_s + 1):
        # print(width)
        for i in range(len_s + 1):
            if i + width == (len_s + 1): break
            j = i + width - 1
            # print("width, i, j = ", width, i, j)

            if(s[i] == s[j] and dp[i+1][j-1]):
                dp[i][j] = 1
                answer = width

    # def isPalindrome(s):
    #     str_s = ""
    #     for i in range(len_s - 1, -1, -1):
    #         str_s += s[i]
    #     # print(s, str_s)
    #     if s == str_s:
    #         return True
    #     return False




    return answer