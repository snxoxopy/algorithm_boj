from collections import deque

n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# [[101111], [101010], [101011], [111011]]
arr = [[] for _ in range(n)]

for i in range(n):
    for e in input():
        arr[i].append(int(e))
# [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]

dr, dc = [0, -1, 0, 1], [-1, 0, 1, 0]

q = deque([[0, 0]])
visited = [[0 for _ in range(m)] for _ in range(n)]
visited[0][0] = 1

while q:
    r, c = q.popleft()
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if -1 < nr < n and -1 < nc < m:
            # print(nr, nc)
            # try:
            #     print("Try")
            #     print(visited[nr][nc])
            #     print("Try")
            #     print(arr[nr][nc])
            # except:
            #     print("except")
            #     print(nr, nc)
            if visited[nr][nc] == 0 and arr[nr][nc] == 1:
                visited[nr][nc] = visited[r][c] + 1
                q.append([nr, nc])

print(visited[n-1][m-1])