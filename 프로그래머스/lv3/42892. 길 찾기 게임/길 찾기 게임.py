import sys
sys.setrecursionlimit(10**6)

def preOrder(arrP, answer):
    nodeinfo = arrP[0] # p-node = [C, R, #node]
    pc, pr, nodeNum = nodeinfo[0], nodeinfo[1], nodeinfo[2]
    C1 = []
    C2 = []
    
    for i in range(1, len(arrP)):
        # C 작은 값 먼저 넣기
        if arrP[i][0] < pc:
            C1.append(arrP[i])
        else:
            C2.append(arrP[i])
            
    answer.append(nodeNum)
    
    if len(C1) > 0:
        preOrder(C1, answer)
    if len(C2) > 0:
        preOrder(C2, answer)
    return

def postOrder(arrP, answer):
    nodeinfo = arrP[0] # p-node = [C, R, #node]
    pc, pr, nodeNum = nodeinfo[0], nodeinfo[1], nodeinfo[2]
    C1 = []
    C2 = []
    for i in range(1, len(arrP)):
        # C값이 작은 것
        if arrP[i][0] < pc:
            C1.append(arrP[i])
        else:
            C2.append(arrP[i])
    
    if len(C1) > 0:
        postOrder(C1, answer)
    if len(C2) > 0:
        postOrder(C2, answer)
        
    answer.append(nodeNum)
    return

def solution(nodeinfo):
    preanswer = []
    postanswer = []
    
    preanswer = []
    postanswer = []
    
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    
    # arrR = [r, c] -> r이 큰 순서로 정렬
    arrP = sorted(nodeinfo, key = lambda x:(-x[1], x[0]))
    # arrPo = sorted(nodeinfo)
    # print(arrP)

    
    preOrder(arrP, preanswer)
    postOrder(arrP, postanswer)
    
    return [preanswer, postanswer]