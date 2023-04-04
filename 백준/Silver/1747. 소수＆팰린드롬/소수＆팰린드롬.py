n = int(input())

def isPrime(num):
    if num == 1: return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
# # Test
# if isPrime(1):
#     print("Prime")
# else: print("No")

def isPalindrome(num):
    #res = [] #LIFO
    res = []
    tmp = num
    while tmp:
        res.append(tmp % 10)
        # print(tmp % 10)
        tmp //= 10

    s = ""
    for c in res:
        s += str(c)
    if int(s) == num: return True
    return False

# print(isPalindrome(79197))

answer = 0
if n == 1: answer = 2
else:
    for num in range(n, 1003002):
        if isPalindrome(num):
            if isPrime(num):
                answer = num
                break

print(answer)