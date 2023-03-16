a, b = map(int, input().split())
prod = a * b
while b:
    if a > b:
        a, b = b, a
    b %= a

print(prod // a)
