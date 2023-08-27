from itertools import permutations
def is_pal(num):
    cnt = 0
    if num < 2:
        return False
    else:
        if num != 2 and num % 2 == 0:
            return False
        else:
            for i in range(3, num):
                if num % i == 0:
                    cnt += 1
            if cnt == 0: return True
            else: return False

def solution(numbers):
    answer = 0
    # permutation
    set_num = set()
    for length in range(1, len(numbers) + 1):
        pmt_num = list(permutations(numbers, length))
        
        # print(pmt_num)
        for nums in pmt_num:
            int_num = 0
            str_num = str()
            for i in nums:
                str_num += str(i)
                # print(str_num)
            int_num = int(str_num)
            set_num.add(int_num)
            # print(int_num)
            # print(set_num)
    for nums in set_num:
        if is_pal(nums):
            # print(nums)
            answer += 1
    
    return answer