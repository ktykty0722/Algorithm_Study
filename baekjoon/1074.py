n, r, c = map(int, input().split())
ans = 0

for i in reversed(range(n)):
    if r < 2 ** i and c < 2 ** i:
        ans += (2 ** i) * (2 ** i) * 0
    elif r < 2 ** i <= c:
        ans += (2 ** i) * (2 ** i) * 1
        c -= 2 ** i
    elif c < 2 ** i <= r:
        ans += (2 ** i) * (2 ** i) * 2
        r -= 2 ** i
    else:
        ans += (2 ** i) * (2 ** i) * 3
        r -= 2 ** i
        c -= 2 ** i

print(ans)
