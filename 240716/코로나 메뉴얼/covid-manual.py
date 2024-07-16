a_cold, a_temp = input().split()
b_cold, b_temp = input().split()
c_cold, c_temp = input().split()
a_temp, b_temp, c_temp = int(a_temp), int(b_temp), int(c_temp)

cnt = 0

if a_cold=="Y" and a_temp>=37:
    cnt += 1

if b_cold=="Y" and b_temp>=37:
    cnt += 1

if c_cold=="Y" and c_temp>=37:
    cnt += 1

if cnt>=2:
    print("E")
else:
    print("N")