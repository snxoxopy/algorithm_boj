from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]
    dist = [-1 for _ in range(n + 1)]
    # [arrivals, step]
    q = deque([[destination, 0]])
    dist[destination] = 0
    
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    
    while q:
        arrv, step = q.popleft()
        for depar in graph[arrv]:
            if dist[depar] == -1:
                dist[depar] = step + 1
                q.append([depar, step + 1])
    
    
    return [dist[i] for i in sources]