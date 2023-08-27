def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')
    pre_e = 0
    for e in arr:
        
        if answer:
            if pre_e != e:
                answer.append(e)
        else:
            answer.append(e)
        pre_e = e
    return answer