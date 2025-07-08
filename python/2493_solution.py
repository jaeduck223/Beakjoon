n = int(input())                               # 탑 개수
h = list(map(int, input().split()))            # 탑 높이
a = []                                     
b = [0] * n                                  

for i in range(n):                            
    while a and h[a[-1]] <= h[i]:
        a.pop()
    
    b[i] = a[-1] + 1 if a else 0
    a.append(i)

print(*b)                                   
