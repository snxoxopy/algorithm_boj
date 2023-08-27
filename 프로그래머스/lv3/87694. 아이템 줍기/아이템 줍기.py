from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]
    # edge = 0, background = -1, area = 1
    arr = [[-1 for _ in range(101)] for _ in range(101)]
    visited = [[0 for _ in range(101)] for _ in range(101)]
    
    for pos in rectangle:
        lr, lc, rr, rc = map(lambda x: 2*x, pos)
        for i in range(lr, rr + 1):
            for j in range(lc, rc + 1):
                if lr < i < rr and lc < j < rc:
                    arr[i][j] = 1
                elif arr[i][j] != 1:
                    arr[i][j] = 0
    # print(arr)
    q = deque([[characterX*2, characterY*2]])
    visited[characterX*2][characterY*2] = 1
    # BFS
    while q:
        r, c = q.popleft()
        if r == itemX * 2 and c == itemY * 2:
            answer = visited[r][c] // 2
            break
        # print(r, c)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if -1 < nr < 101 and -1 < nc < 101 and arr[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                q.append([nr, nc])
                
                    # return answer
    
#     # answer = max(*zip(visited)) // 2
#     # a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     # print(max(map(max, a)))
#     answer = max(map(max, visited)) // 2
    
    return answer