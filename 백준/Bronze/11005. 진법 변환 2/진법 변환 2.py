N, B = map(int, input().split())
lst_q = []
while N:
    q = N % B
    # print(q)
    lst_q.append(q)
    N //= B
# print(lst_q)
ch = dict()
for i in range(10, 36):
    ch[i] = chr(i + 55)
# print(ch)
answer = str()
for i in range(len(lst_q)):
    num = lst_q[len(lst_q) - i - 1]
    if num > 9:
        answer += ch[num]
        # print(ch[num])
    else:
        answer += str(num)

print(answer)