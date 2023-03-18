n = int(input())
arr = []
for i in range(n):
    arr.append([int(j) for j in input()])

dp = [[[0] * 10 for _ in range(n)] for _ in range(1 << n)]


def dfs(now, artist, cost):
    if dp[now][artist][cost] != 0:
        return dp[now][artist][cost]

    cnt = 0
    for i in range(1, n):
        if arr[artist][i] >= cost and now & (1 << i) <= 0:
            cnt = max(cnt, 1 + dfs(now | (1 << i), i, arr[artist][i]))
    dp[now][artist][cost] = cnt

    return cnt


print(dfs(1, 0, 0) + 1)
