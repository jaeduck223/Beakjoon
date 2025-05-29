n, k = map(int, input().split())
a = list(range(1, n + 1))

result = []
b = 0

while a:
    b = (b + k - 1) % len(a) 
    result.append(a.pop(b))      

print("<" + ", ".join(map(str, result)) + ">")

