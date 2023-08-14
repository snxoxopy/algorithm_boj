import heapq

def solution(jobs):
    answer = 0
    hq = []
    i = 0
    t_start, t_load, t_end = -1, 0, 0
    
    while i < len(jobs):
        for t_req, t_span in jobs:
            # print(t_end)
            if t_start < t_req <= t_end:
                heapq.heappush(hq, [t_span, t_req])
        if hq:
            t_span, t_req = heapq.heappop(hq)
            t_start = t_end
            t_load = t_span + abs(t_start - t_req)
            t_end = t_start + t_span

            answer += t_load
            i += 1
        else:
            t_end += 1
    answer //= len(jobs)
    return answer