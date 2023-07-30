from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    q = deque()
    graph = [[] for _ in range(n + 1)]
    v = [-1 for _ in range(n + 1)]
    v[destination] = 0
    
    
    for start, end in roads:
        graph[start].append(end)
        graph[end].append(start)
    
    q.append([destination, 0])
        
    while q:
        cur, prev = q.popleft()
        for node in graph[cur]:
            if v[node] == -1:
                q.append([node, prev + 1]) 
                v[node] = prev + 1
    
    # answer = [0 for _ in range(len(sources))]
    # i = 0
    # for s in sources:
    #     if s == destination:
    #         answer[i] = 0
    #         continue
    #     answer[i] = v[s]
    #     i += 1
    return [v[i] for i in sources]