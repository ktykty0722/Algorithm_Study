from collections import deque

n = int(input())
k = int(input())
apple = []
rot = {}
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
for _ in range(k):
    a, b = map(int, input().split())
    apple.append((a, b))
l = int(input())
for _ in range(l):
    a, b = map(str, input().split())
    rot[int(a)] = b

ans = 0
q = deque()
q.append((1, 1))
y, x = 1, 1
dirs = 0
while 1:
    ans += 1
    ny = y + dy[dirs]
    nx = x + dx[dirs]
    if 1 <= ny <= n and 1 <= nx <= n and q.count((ny, nx)) == 0:
        if (ny, nx) not in apple:
            q.pop()
        else:
            apple.remove((ny, nx))
        q.appendleft((ny, nx))

        y = ny
        x = nx
    else:
        break

    if ans in rot.keys():
        if rot[ans] == 'L':
            dirs = (dirs + 3) % 4
        else:
            dirs = (dirs + 1) % 4

print(ans)
