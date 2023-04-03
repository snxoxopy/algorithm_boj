"""
---
title:  "[Python] BOJ_2178_미로_탐색"
excerpt: "https://www.acmicpc.net/problem/2178"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - BOJ
  - BFS
---

문제 이해: 5분
구현: 50분
Debug: 12분
참고 자료
https://yuna0125.tistory.com/61
"""

import sys

from collections import deque

#sys.stdin = open("input.txt", "r")
n, m = map(int, sys.stdin.readline().split())

# print(n, m)

arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
# for _ in range(n):
#     arr.append(list(map(int, sys.stdin.readline().split())))
# print(arr)

#(0,0)에서 시작

# E W S N
dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)


answer = 0
q = deque([[0, 0]])
visited = [[0 for _ in range(m)] for _ in range(n)]
# print(visited)
visited[0][0] = 1
while q:
    [r, c] = q.popleft()
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        # print(nr, nc)
        if -1 < nr < n and -1 < nc < m and arr[nr][nc] == 1:
            arr[nr][nc] = arr[r][c] + 1
            q.append([nr, nc])
            # print(q)
            # r, c = nr, nc
answer = arr[n-1][m-1]

print(answer)

