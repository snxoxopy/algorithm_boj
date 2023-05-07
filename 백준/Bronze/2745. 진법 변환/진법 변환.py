N, B = map(str, input().split())

lst_n = []
for c in N:
    if 64 < ord(c) < 91:
        lst_n.append(ord(c) - ord('A') + 10)
    else:
        lst_n.append(int(c))

answer = 0

for i in range(len(lst_n)):
    num = lst_n[len(lst_n) -i -1]
    carry = int(B) ** i
    answer += (num * carry)

print(answer)