n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

ans = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            ans[i][j] += a[i][l] * b[l][j]

for i in ans:
    print(*i)
