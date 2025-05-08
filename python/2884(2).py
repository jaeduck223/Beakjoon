h,m = map(int, input("입력 ").split())

if ((m - 45) < 0) and ((h - 1) >= 0):
    print("정답",h-1,m +15)
elif ((m - 45) == 0):
    print("정답",h,(m - 45))
elif((m - 45) < 0) and ((h - 1) < 0):
    print("정답",h + 23,m+15)
else:
    print("정답",h,m - 45)
