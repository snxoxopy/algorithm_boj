def solution(gems):
    answer = [0, len(gems)]
    size = len(set(gems))
    left, right = 0, 0
    gem_dict = {gems[0]: 1}
    
    while left < len(gems) and right < len(gems):
        if len(gem_dict) == size:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            else:
                gem_dict[gems[left]] -= 1
                if gem_dict[gems[left]] == 0:
                    del gem_dict[gems[left]]
                    
                left += 1
        else:
            right += 1
            if right == len(gems):
                break
            
            if gems[right] in gem_dict:
                gem_dict[gems[right]] += 1
            else:
                gem_dict[gems[right]] = 1
    
    return [answer[0] + 1, answer[1] + 1]
    """

    for start in range(len(gems) - 1):
        ugem = list(set(gems))
        # print(ugem)
        for end in range(start, len(gems)):
            # print(ugem, gems[end])
            if gems[end] in ugem:
                ugem.remove(gems[end])
            if not ugem:
                answer.append([start + 1, end + 1])
                # print("END")
                break
    
    min_val = float("inf")
    for i in range(len(answer)):
        start, end = answer[i]
        min_val = min(end-start, min_val)
    
    for start, end in answer:
        if end - start == min_val:
            answer = [start, end]
            break
    
    
    return answer
    """