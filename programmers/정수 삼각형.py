def solution(triangle):
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        dp[i][0] = triangle[i][0] + dp[i-1][0]
        for j in range(1, len(triangle[i])):
            dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
        dp[i][len(triangle[i])-1] = triangle[i][len(triangle[i])-1] + dp[i-1][len(triangle[i])-2]
    return max(dp[len(triangle)-1])
