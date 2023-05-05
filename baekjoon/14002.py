import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
x = max(dp)
ans = []
for i in reversed(range(n)):
    if dp[i] == x:
        ans.append(arr[i])
        x -= 1
ans.reverse()
print(*ans)
