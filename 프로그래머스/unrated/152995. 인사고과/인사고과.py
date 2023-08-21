def solution(scores):
    answer = 0
    target_a, target_b, target_ab = scores[0][0], scores[0][1], sum(scores[0])
    max_score = 0
    scores.sort(key=lambda x: [-x[0], x[1]])
    for a, b in scores:
        # print(a, b)
        # 어떤 사원이 다른 임의의 사원보다 두 점수가 모두 낮은 경우가 한 번이라도 있다면
        if a > target_a and b > target_b:
            # print(a, '>', target_a, b, '>', target_b)
            return -1
        if b >= max_score:
            max_score = b
            if a + b > target_ab:
                answer += 1
    return answer + 1