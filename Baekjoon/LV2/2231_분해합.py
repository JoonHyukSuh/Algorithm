#2231 분해합 
n = int(input())

for i in range(1,n+1):
  n_list = list(map(int,str(i)))
  result = i + sum(n_list)
  if result == n:
    print(i)
    break
  if n == i:
    print(0)
    break

  

