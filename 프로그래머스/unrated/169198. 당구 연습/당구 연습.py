from collections import deque

def solution(m, n, startX, startY, balls):
    answer = []
    
    # SX, SY = sc, sr
    sc, sr = startX, startY
    
    
    q = deque()
    for nc, nr in balls:
        res = float('INF')
        # print(nr, nc)
        # 상
        if not (nr < sr and nc == sc):
            q.append([-1 * nr, nc])
        
        # 하
        if not (nr > sr and nc == sc):
            q.append([2 * n - nr, nc])
        
        # 좌
        if not (nr == sr and nc < sc):
            q.append([nr, -1 * nc])
            
        # 우
        if not (nr == sr and nc > sc):
            q.append([nr, 2 * m - nc])
        
        # print(q)
        while q:
            br, bc = q.popleft()
            diff_r = abs(sr - br)
            diff_c = abs(sc - bc)
            dist = diff_r ** 2 + diff_c ** 2
            res = min(res, dist)
        answer.append(res)
    
    return answer