t = int(input())
for _ in range(t):
  k = int(input())
  n = int(input())
  floor = [i+1 for i in range(n+1)]
  
  for i in range(k):
    for j in range(1,n+1):
      floor[j] += floor[j-1]
  print(floor[n-1])