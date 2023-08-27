def solution(sizes):
    answer = 0
    weights = []
    heights = []
    
    # sizes = [min_size, max_size]
    # max(min_size) * max(max_size)
    for size in sizes:
        size.sort()
        # print(size)
    # print(sizes)
    # print(max(sizes, key=lambda x: x[0])[0])
    answer = max(sizes, key=lambda x : x[1])[1] * max(sizes, key=lambda x : x[0])[0]

    return answer