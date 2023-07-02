from collections import defaultdict
def solution(weights):
    answer = 0
    len_w = len(weights)
    dict_w = defaultdict(int)
    
    for w in weights:
        dict_w[w] += 1
    
    # print(dict_w.items())
    for key, val in dict_w.items():
        # print(key, val)
        if val > 1:
            answer += val * (val - 1) // 2
        if key * 2 in dict_w:
            answer += val * dict_w[key*2]
        if key * 3 % 2 == 0 and key * 3 // 2 in dict_w:
            answer += val * dict_w[key*3 // 2]
        if key * 4 % 3 == 0 and key * 4 // 3 in dict_w:
            answer += val * dict_w[key*4 // 3]
    
    return answer