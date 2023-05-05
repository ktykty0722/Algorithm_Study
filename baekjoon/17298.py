n = int(input())
arr = list(map(int, input().split()))
ans = [-1] * n
st = []

for i in range(n):
    while st and arr[st[-1]] < arr[i]:
        ans[st.pop()] = arr[i]
    st.append(i)

print(*ans)
