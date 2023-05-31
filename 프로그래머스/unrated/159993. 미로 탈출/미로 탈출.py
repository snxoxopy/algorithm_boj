from collections import deque

def solution(maps):
    
    # 2D 미로 탈출 최소시간 -> BFS 
    q = deque()
    
    # 이동 가능 경우의 수
    dr, dc = (0, -1, 0, 1), (-1, 0, 1, 0)
    
    # 방문 누적 날짜
    visited_off = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited_on = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    flag = False
    day = 0
    
    # 출발 지점 찾기
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                q.append([i, j, day, flag])

    
    while q:
        r, c, day, flag = q.popleft()
        
        if not flag:
            visited_off[r][c] = 1
        else:
            visited_on[r][c] = 1
                
        # Case) L
        if maps[r][c] == 'L':
            flag = True
            visited_on[r][c] = 1
            
        # Case) Exit and opened
        if flag and maps[r][c] == 'E':
            return day
        
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            # Case) not X
            if -1 < nr < len(maps) and -1 < nc < len(maps[0]) and maps[nr][nc] != 'X':      
                if not flag:
                    if not visited_off[nr][nc]:
                        visited_off[nr][nc] = 1
                        q.append([nr, nc, day + 1, flag])
                else:
                    if not visited_on[nr][nc]:
                        visited_on[nr][nc] = 1
                        q.append([nr, nc, day + 1, flag])
            
    return -1