s = input()
stack = []
tag = False
ans = ''
for i in s:
    if i == '>':
        tag = False
        ans += i
    elif i == '<':
        while stack:
            ans += stack.pop()
        ans += i
        tag = True
    elif i == ' ':
        while stack:
            ans += stack.pop()
        ans += i
    elif tag:
        ans += i
    else:
        stack.append(i)

while stack:
    ans += stack.pop()

print(ans)
