n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
ans = 0

for i in range(0, n):
    ans = max(ans, arr[i] + i + 1)

print(ans + 1)
