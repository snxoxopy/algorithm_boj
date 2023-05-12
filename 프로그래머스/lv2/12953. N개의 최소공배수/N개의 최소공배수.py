def gcd(a, b):
    if a % b == 0:
        return b 
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def solution(arr):
    answer = arr[0]
    for n in arr:
        answer = lcm(n , answer)
    return answer