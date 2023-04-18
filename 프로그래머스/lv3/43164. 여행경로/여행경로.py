from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    visited = defaultdict(list)
    
    start = "ICN"
    step = len(tickets) + 1
    
    answer = []

    for boarding_pass in tickets:
        graph[boarding_pass[0]].append(boarding_pass[1])
        visited[boarding_pass[0]].append(False)

    # print(graph)
    
    def dfs(depart, itinerary):
        nonlocal step
        if len(itinerary) == step:
            answer.append(itinerary)
            return 0
        for j in range(len(graph[depart])):
            if not visited[depart][j]:
                arrive = graph[depart][j]
                visited[depart][j] = True
                dfs(arrive, itinerary + [arrive])
                visited[depart][j] = False
    # main
    for i in range(len(graph[start])):
        cur = graph[start][i]
        visited[start][i] = True
        dfs(cur, [start, cur])
        visited[start][i] = False

    answer.sort()
    # print(answer)
    return answer[0]