from collections import deque

def solution(maps):
    answer = 0
    dr, dc = (0, 0, 1, -1), (1, -1, 0, 0)
    
    n, m = len(maps), len(maps[0])
    
    def bfs(q):
        cnt = 0
        visited = [[0] * m for _ in range(n)]
        visited[0][0] = 1
        while(q):
            r, c = q.popleft()
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if -1 < nr < n and -1 < nc < m and maps[nr][nc] == 1:
                    if not visited[nr][nc]:
                        q.append([nr, nc])
                        visited[nr][nc] = visited[r][c] + 1
        return visited
                        
    v = bfs(deque([[0,0]]))
    answer = v[n-1][m-1]
    answer = -1 if answer == 0 else answer
    return answer