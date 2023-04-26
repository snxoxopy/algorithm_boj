# def mkbin(num):
#     n_bin = ''
#     cn = num
#     while cn:
#         r = cn % 2 
#         n_bin += str(r)
#         cn //= 2
    
#     n_bin = list(reversed(n_bin))
#     n_bin = list(map(int, n_bin))
#     print(n_bin)
#     one_bin = sum(n_bin)
#     return one_bin
    

def solution(n):
    answer = 0
    
    i = 0
    # orig_bin = mkbin(n)
    # print(bin(n).count('1'))
    
    orig_bin = bin(n).count('1')
    for i in range(n+1, 1000001):
        # i += 1
        # new_bin = mkbin(i)
        new_bin = bin(i).count('1')
        if orig_bin == new_bin:
            answer = i
            break
        
    
    return answer