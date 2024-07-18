a, b = map(float, input().split())

print(a/b, end='')
for i in range(2, 21):
    # a *= 10
    k = int(a//b)
    print(k, end='')