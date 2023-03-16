from itertools import combinations

n, m = map(int, input().split())
arr = [[False] * n for _ in range(n)]

for i in range(m):
    m1, m2 = map(int, input().split())
    arr[m1 - 1][m2 - 1] = True
    arr[m2 - 1][m1 - 1] = True

ans = 0

for i in combinations(range(n), 3):
    if arr[i[0]][i[1]] or arr[i[0]][i[2]] or arr[i[1]][i[2]]:
        continue
    ans += 1

print(ans)
