import sys
from collections import deque

m, n, h = map(int, input().split())
arr = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]
q = deque()
ans = 0

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    while q:
        z, y, x = q.popleft()
        visited[z][y][x] = False
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if arr[nz][ny][nx] == 0 and not visited[nz][ny][nx]:
                    q.append((nz, ny, nx))
                    arr[nz][ny][nx] = arr[z][y][x] + 1
                    visited[nz][ny][nx] = False


for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append((i, j, k))
bfs()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                print(-1)
                exit(0)
            ans = max(ans, arr[i][j][k])

print(ans - 1)
