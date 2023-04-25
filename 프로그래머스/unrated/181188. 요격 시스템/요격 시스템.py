def solution(targets):
    answer = 0
    
    targets.sort(key = lambda x: [x[1], x[0]])

    '''
    targets.sort(key=lambda x: x[1])
    globalMax = targets[-1][1]
    targets.sort(key=lambda x: x[0])
    globalMin = targets[0][0]
    #print(f"{globalMin} {globalMax}")
    allXcoordi = list()
    for item in targets:
        allXcoordi += range(item[0], item[1])
    #print(allXcoordi)
    dictToCount = dict()
    answerList = list()
    Xrange = list(range(globalMin, globalMax))
    #count and find only case start
    for item in Xrange:
        dictToCount[item] = 0
        for X in allXcoordi:
            if item == X: dictToCount[item] += 1
        if dictToCount[item] == 1: answerList.append(item)
    for item in answerList:
        Xrange.remove(item)
    print(answerList)
    #count and find only case end
    '''
    
    
    targets.sort(key=lambda x: [x[1], x[0]])
    # print(targets)
    # os, oe = targets[0]
    os, oe = 0, 0
    for s, e in targets:
        # # oe - os < oe
        # if oe - os > e - s:
        #     os, oe = s, e
        #     answer += 1
        if oe <= s:
            oe = e
            answer += 1
            
        # if oe - 1 == s: answer += 1
    
        
    
    '''
    lst = [[] for _ in range(len(targets))]
    # lst[0].append(1)
    # lst[1].append(2)
    
    # print(lst)
    num = []
    
    
    max_s, min_e = 0, 10**9
    for i in range(len(targets)):
        s, e = targets[i]
        max_s, min_e = max(max_s, e), min(min_e, s)
        
    print(min_e, max_s)
    for i in range(min_e, max_s):
        num.append(i)
    cnt = [0] * len(num)
    for s, e in targets:
        for n in num:
            print(s, e, n)
            if s - 1 < n < e + 1:
                cnt[n-1] += 1
    print(cnt)
    
    # print(num)
    '''
    
    return answer