s = input().replace(' ', '')
ucpc = 'UCPC'
idx = 0

for i in s:
    if i == ucpc[idx]:
        idx += 1
    if idx == 4:
        print("I love UCPC")
        break
else:
    print("I hate UCPC")