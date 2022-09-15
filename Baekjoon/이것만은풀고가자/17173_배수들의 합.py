#17173 배수들의 합
n,m = map(int,input().split())

k_list = list(map(int,input().split()))
res = 0
for i in range(1,n+1):
  for n in k_list:
    if i % n == 0:
      res += i
      break
print(res)