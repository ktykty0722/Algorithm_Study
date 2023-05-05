n, m = map(int, input().split())
ans = 0
s = []
for _ in range(n):
    s.append(input().rstrip())
for _ in range(m):
    temp = input().rstrip()
    if temp in s:
        ans += 1
print(ans)
