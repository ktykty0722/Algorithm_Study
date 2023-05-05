func = input()
st = []
ans = []

for s in func:
    if s.isalpha():
        ans.append(s)
    else:
        if s == '(':
            st.append(s)
        elif s == ')':
            while st and st[-1] != '(':
                ans.append(st.pop())
            st.pop()
        elif s == '+' or s == '-':
            while st and st[-1] != '(':
                ans.append(st.pop())
            st.append(s)
        elif s == '*' or s == '/':
            while st and (st[-1] == '*' or st[-1] == '/'):
                ans.append(st.pop())
            st.append(s)
while st:
    ans.append(st.pop())

print(''.join(ans))