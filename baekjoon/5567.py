from collections import deque


def bfs(x):
    q = deque()
    visited[x] = 1
    q.append(x)
    while q:
        now = q.popleft()
        for i in arr[now]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[now] + 1


n = int(input())
m = int(input())
arr = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


bfs(1)
ans = 0
for i in range(2, n + 1):
    if 1 <= visited[i] <= 3:
        ans += 1

print(ans)
