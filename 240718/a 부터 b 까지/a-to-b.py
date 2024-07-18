a, b = map(int, input().split())

for i in range(a, b+1):
    if a<=b:
        print(a, end=' ')
        if i%2==1:
            a *= 2
        elif i%2==0:
            a += 3