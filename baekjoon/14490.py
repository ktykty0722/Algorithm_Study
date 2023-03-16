def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


n, m = map(int, input().split(':'))
temp = gcd(n, m)
print(str(n//temp) + ":" + str(m//temp))
