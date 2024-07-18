n = int(input())

for i in range(1, n+1):
    if i%3==0 or i - (i//10)*10 == 3 or i - (i//10)*10== 6 or i - (i//10)*10 == 9:
        print(0, end=' ')
    else:
        print(i, end=' ')
    i += 1