a, b = map(int, input().split())


# print(f"{a//b}.", end='')
for i in range(21):
    quot = a//b
    remain = a%b
    a = remain*10
    print(quot, end='')

    if i==0:
        print(".", end='')