def solution(n, s):
    if n > s:
        return [-1]

    ans = [s // n for _ in range(n)]
    for i in range(s % n):
        ans[i] += 1
    ans.sort()
    return ans
