import math
a,b,c = map(int, input("").split())

if (a == b == c): #3개 다 맞는 경우
    print(10000+(a * 1000))
elif (a == b) or (b == c) or (a == c): #2개만 맞는 경우
    if (a==b):
        print(1000 + (a*100))
    elif (b == c):
        print(1000 + (b*100))
    elif (c == a):
        print(1000 + (c*100))
else:   #한 개도 안 맞는 경우
    print(max(a,b,c)*100)
