def func(string, cnt):
    if len(string) > 1:
        cnt += 1
        temp = 0
        for i in string:
            temp += int(i)
        func(str(temp), cnt)
    else:
        print(cnt)
        if int(string) % 3 == 0:
            print("YES")
        else:
            print("NO")


x = input()
c = 0
func(x, c)
