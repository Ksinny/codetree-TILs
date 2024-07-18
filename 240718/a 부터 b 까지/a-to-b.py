a, b = map(int, input().split())


# break, continue 사용X
for i in range(a, b+1):
    if a*2<=b or a+3<=b:
        print(a, end=' ')
        if i%2==1:
            a *= 2
        elif i%2==0:
            a += 3

print(a)