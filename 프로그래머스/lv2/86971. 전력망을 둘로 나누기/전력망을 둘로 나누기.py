from collections import deque
def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n)]
    for start, end in wires:
        graph[start - 1].append(end - 1)
        graph[end - 1].append(start - 1)
    
    for start in range(n):
        for end in graph[start]:
            if not end: continue
            cut = [[0 for _ in range(n)] for _ in range(n)]
            cut[start][end] = 1
           
            visited = [0 for _ in range(n)]
            q = deque([start])
            visited[start] = 1
            
            # 기준 node 영역을 선 방문처리 했으므로 1부터 시작
            cnt = 1
            while q:
                n_cur = q.popleft()
                for n_nxt in graph[n_cur]:
                    visited[n_cur] = 1
                    if not visited[n_nxt] and not cut[n_cur][n_nxt]:
                        visited[n_nxt] = 1
                        q.append(n_nxt)
                        cnt += 1
            # 기준 node에서 개수 세기 끝난 시점
            area1 = n - cnt
            area2 = n - area1
            # |area1 - area2|가 가장 작은 값 반환
            answer = min(abs(area1 - area2), answer)
    return answer