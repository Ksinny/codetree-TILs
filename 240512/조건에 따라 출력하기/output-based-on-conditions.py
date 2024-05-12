n = int(input())

for i in range(1, n+1):
    a = int(input())
    if a == 0:
        break

    if a%3 == 0:
        print(a//3)
    else:
        print(a+2)