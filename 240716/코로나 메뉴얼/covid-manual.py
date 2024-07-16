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

# A가 2명 이상인지 판단하기
# if c1 == 'Y' and t1 >= 37:
#     # 첫 번째 사람이 A라면, 남은 두 사람 중 한 사람이라도 A면 됩니다.
#     if (c2 == 'Y' and t2 >= 37) or (c3 == 'Y' and t3 >= 37):
#         print("E")
#     else:
#         print("N")
# else:
#     # 첫 번째 사람이 A가 아니라면, 남은 두 사람 모두 A여야만 합니다.
#     if (c2 == 'Y' and t2 >= 37) and (c3 == 'Y' and t3 >= 37):
#         print("E")
#     else:
#         print("N")