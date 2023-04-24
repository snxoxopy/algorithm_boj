from collections import deque

def solution(n, computers):
    answer = 0
    
    v = [0] * n
    area = 1
    
    def bfs(node):
        nonlocal area
        q = deque([node])
        
        while q:
            n1 = q.popleft()
            # v[n1] = area
            for n2 in range(n):
                if computers[n1][n2] and v[n2] == 0:
                    v[n2] = area
                    q.append(n2)
        print(v)
        return v
                    
    for n1 in range(n):
        answer = bfs(n1)
        area += 1
        
    
    answer = len(set(answer))

    return answer