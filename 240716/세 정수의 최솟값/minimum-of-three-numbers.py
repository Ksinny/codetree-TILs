a, b, c = map(int, input().split())
arr = [a, b, c]

# print(min(arr))


# 단순 if문

if a<=b:
    mi = a
else:
    mi = b

if c<=mi:
    mi = c

print(mi)
    


# mi = a if a<=c else (b if b<=c else c)
# print(mi)