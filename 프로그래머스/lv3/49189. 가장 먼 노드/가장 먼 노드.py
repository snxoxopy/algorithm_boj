from collections import deque
def solution(n, edge):
    answer = 0
    q = deque()
    edge.sort()
    # edge = sorted(edge, key = lambda x : x[1])
    # print(edge)
    graph = [[] for _ in range(n + 1)]
    v = [0 for _ in range(n + 1)]
    
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
    
    v[1] = 1
    q.append((1))

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not v[nxt]:
                v[nxt] = v[cur] + 1
                q.append(nxt)
    print(v)
    for i in range(n + 1):
        if v[i] == max(v):
            answer += 1

    return answer