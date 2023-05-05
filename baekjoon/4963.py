import sys
sys.setrecursionlimit(10000)
dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]


def dfs(y, x):
    visited[y][x] = True;
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < h and 0 <= nx < w:
            if not visited[ny][nx] and graph[ny][nx] == 1:
                dfs(ny, nx)


while True:
    ans = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    visited = [[False] * w for _ in range(h)]
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                ans += 1
    print(ans)
