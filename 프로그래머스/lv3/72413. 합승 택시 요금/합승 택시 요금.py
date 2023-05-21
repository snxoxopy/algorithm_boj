def solution(n, s, a, b, fares):

    INF = float('inf')
    
    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    
    for i in range(n + 1):
        graph[i][i] = 0
    
    for node1, node2, price in fares:
        # print(node1, node2, price)
        graph[node1][node2] = price
        graph[node2][node1] = price
    # print(graph)
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if graph[j][k] > graph[j][i] + graph[i][k]:
                    graph[j][k] = graph[j][i] + graph[i][k]
    
    answer = INF
    for i in range(1, n + 1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
    
    return answer