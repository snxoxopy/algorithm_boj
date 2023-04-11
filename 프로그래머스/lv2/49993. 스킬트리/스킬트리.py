def solution(skill, skill_trees):
    answer = 0
    def isPossible(skill, tree):
        visited = [0] * len(skill)
        for c in tree:
            for i in range(len(skill)):
                if i == 0 and c == skill[i]:
                    visited[i] = 1
                if i > 0:         
                    if c == skill[i] and visited[i - 1]:
                        visited[i] = 1
                    elif c == skill[i] and not visited[i - 1]:
                        visited[i] = 0
                        return False
        
        # print(visited)
        return True
                    
    
    for tree in skill_trees:
        if isPossible(skill, tree):
            print(tree)
            answer += 1
    
    
    return answer