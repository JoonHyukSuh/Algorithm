from itertools import permutations
n = int(input())
per = list(permutations([i+1 for i in range(n)])) #('3','6','9') 이런 식으로 모든 조합 저장 
for i in per:
  for j in i:
    print(j,end=' ')
  print()