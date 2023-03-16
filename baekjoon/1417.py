n = int(input())
dasom = int(input())
arr = []
ans = 0

for _ in range(n-1):
    arr.append(int(input()))

arr.sort(reverse=True)
if n == 1:
    print(0)
else:
    while arr[0] >= dasom:
        arr[0] -= 1
        dasom += 1
        ans += 1
        arr.sort(reverse=True)
    print(ans)
