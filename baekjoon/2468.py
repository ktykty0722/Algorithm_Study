import sys
sys.setrecursionlimit(100000)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(y, x):
    visited[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if arr[ny][nx] > t and not visited[ny][nx]:
                dfs(ny, nx)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
ans = 0
for t in range(101):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > t and not visited[i][j]:
                dfs(i, j)
                cnt += 1
    ans = max(ans, cnt)
print(ans)
