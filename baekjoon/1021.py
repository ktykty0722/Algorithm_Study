from collections import deque

n, m = map(int, input().split())
pos = list(map(int, input().split()))
q = deque([i for i in range(1, n + 1)])
ans = 0
for p in pos:
    while True:
        if q[0] == p:
            q.popleft()
            break
        else:
            if q.index(p) <= len(q) // 2:
                q.rotate(-1)
                ans += 1
            else:
                q.rotate(1)
                ans += 1
print(ans)
