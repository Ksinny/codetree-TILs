a, b = map(int, input().split())

for i in range(21):
    k = a//b
    s = a%b
    a = s*10
    print(k, end='')
    
    if i == 0:
        print(".", end='')