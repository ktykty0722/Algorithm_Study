n = int(input())
arr = [input() for _ in range(n)]

arr_inc = sorted(arr)
arr_dec = sorted(arr, reverse=True)

if arr == arr_inc:
    print('INCREASING')
elif arr == arr_dec:
    print('DECREASING')
else:
    print('NEITHER')
