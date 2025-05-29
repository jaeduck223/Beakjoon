N, K = map(int, input().split())

a = list(range(1, N+1))
print(a)

for i in range (N):
    b = a[K-1] #제거 대상 항목 지목
    del a[b]   #제거 실행
    print(b)

    K = K + 1
    print(K)

    c = []     #제거된 것들을 모음
    c.append(b)
    print(c)
