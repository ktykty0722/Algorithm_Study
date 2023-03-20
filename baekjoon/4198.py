n = int(input())
arr = [int(input()) for _ in range(n)]
dp1 = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]
ans = 0

for i in reversed(range(n)):
    for j in range(i + 1, n):
        if arr[j] > arr[i]:
            dp2[i] = max(dp2[i], dp2[j])
        else:
            dp1[i] = max(dp1[i], dp1[j])

    dp1[i] += 1
    dp2[i] += 1
    ans = max(ans, dp1[i] + dp2[i] - 1)

print(ans)
