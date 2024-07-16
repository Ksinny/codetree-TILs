m = int(input())

if m<=2 or m>=12:
    print("Winter")
elif m>=9:
    print("Fall")
elif m>=6:
    print("Summer")
else:
    print("Spring")