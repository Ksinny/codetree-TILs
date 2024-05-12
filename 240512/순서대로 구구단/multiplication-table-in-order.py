a, b = map(int, input().split())

for i in range(1, 10):
    print(a, "*", i, "=", a*i, end='  ')
    print(b, "*", i, "=", b*i)