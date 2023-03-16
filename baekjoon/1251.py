s = input()
ans = []

for i in range(1, len(s) - 1):
    for j in range(i + 1, len(s)):
        temp = s[:i][::-1] + s[i:j][::-1] + s[j:][::-1]
        ans.append(temp)
print(min(ans))
