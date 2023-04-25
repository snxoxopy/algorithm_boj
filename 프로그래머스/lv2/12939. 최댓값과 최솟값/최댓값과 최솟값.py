def solution(s):
    answer = ''
    # lst = s.split()
    lst = list(map(int, s.split()))
    max_num, min_num = max(lst), min(lst)
    answer =  str(min_num) + ' ' + str(max_num) 
    return answer