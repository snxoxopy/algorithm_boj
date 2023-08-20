from itertools import permutations

def solution(weights):
    answer, dict_w = 0, dict()
    nums = [2, 3, 4]
    pos = []
    for w in weights:
        dict_w[float(w)] = 0
    
    for w in weights:
        dict_w[float(w)] += 1
        
    for num in permutations(nums,2):
        if num not in pos:
            pos.append(num)
    
    # 같은 위치에 있을 때
    pos.append([1, 1])
    
    for w in weights:
        dict_w[float(w)] -= 1
        for d1, d2 in pos:
            ratio = w * d1 / d2
            if ratio in dict_w:
                # print(ratio)
                answer += dict_w[ratio]
                
    return answer