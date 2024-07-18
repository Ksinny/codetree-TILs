n = int(input())

for i in range(1, n+1):
    # 3의 배수인 경우
    if i%3==0: 
        print(0, end=' ')
    # 3, 6, 9가 들어가는 경우
    elif i//10==3 or i//10==6 or i//10==9 or i%10==3 or i%10==6 or i%10==9:
        print(0, end=' ')
    else:
        print(i, end=' ')
    i += 1