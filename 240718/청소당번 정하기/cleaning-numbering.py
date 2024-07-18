n = int(input())

d2, d3, d12 = 0, 0, 0

for i in range(1, n+1):
    if i%12==0:
        d12 += 1
    elif i%3==0:
        d3 += 1
    elif i%2==0:
        d2 += 1

print(d2, d3, d12)