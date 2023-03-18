from collections import deque


def bfs(y, x, color):
    cnt = 1
    q = deque()
    q.append((y, x))
    visited[y][x] = True

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx] and color == arr[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = True
                cnt += 1

    return cnt


n, m = map(int, input().split())
arr = [list(input()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
ans1, ans2 = 0, 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            num = bfs(i, j, arr[i][j])
            if arr[i][j] == 'W':
                ans1 += num ** 2
            else:
                ans2 += num ** 2

print(ans1, ans2)
