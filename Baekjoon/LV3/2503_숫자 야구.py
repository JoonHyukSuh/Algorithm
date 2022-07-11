# 2503 숫자야구 - 1주차 공통 문제 (다시 풀기)
from itertools import permutations

n = int(input())
arr = []
for _ in range(n):
  arr.append(list(map(str,input().split())))

per = list(permutations(range(1,10),3)) #('3','6','9') 이런 식으로 모든 조합 저장

for guess, strike, ball in arr:
  new_per = []
    # 327 2 0 
  while per:
      s,b = 0,0
      info = per.pop()
        
      for i in range(3):
          if int(guess[i]) == info[i]:
              s+=1
          elif int(guess[i]) in info:
              b+=1


      if s==int(strike) and b==int(ball):
          new_per.append(info)
  per= new_per

print(len(per))