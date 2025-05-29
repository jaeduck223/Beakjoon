#블랙잭 문제
import random as r      

N,M = map(int, input().split()) #카드의 개수, 딜러의 숫자
cards = list(map(int, input().split()))

n_list = 0

for i in range(N-2):  #1번째 카드
    for j in range(i+1, N-1): #2번째 카드
        for k in range(j+1, N): #3번째 카드
            total= cards[i] + cards[j] +cards[k]
            if total <= M:
                n_list = max(n_list, total)
    
print(n_list)
