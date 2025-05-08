h, m = map(int, input().split())

if ((m - 45) < 0) and ((h - 1) >= 0):
    print(h - 1, m - 45 + 60)
elif ((m - 45) < 0) and ((h - 1) < 0):
    print(h + 23, m - 45 + 60)
else:
    print(h, m - 45)
    
