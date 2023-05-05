n = int(input())
arr = list(map(int, input().split()))
ans = [0] * n
st = []

for i in reversed(range(n)):
    while st and arr[st[-1]] < arr[i]:
        ans[st.pop()] = i + 1
    st.append(i)

print(*ans)
