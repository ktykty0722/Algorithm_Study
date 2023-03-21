n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = []
visited = [[False] * m for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for _ in range(n):
    arr.append(list(map(int, input().split())))

visited[r][c] = True
ans = 1

while 1:
    flag = False
    for _ in range(4):
        ny = r + dy[(d + 3) % 4]
        nx = c + dx[(d + 3) % 4]

        d = (d + 3) % 4

        if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == 0 and not visited[ny][nx]:
            visited[ny][nx] = True
            ans += 1
            r = ny
            c = nx
            flag = True
            break

    if not flag:
        if arr[r - dy[d]][c - dx[d]] == 1:
            print(ans)
            break
        else:
            r = r - dy[d]
            c = c - dx[d]
