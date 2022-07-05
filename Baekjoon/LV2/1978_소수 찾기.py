#1978 소수 찾기
n = int(input())
numbers = list(map(int,input().split()))
count = 0
for i in numbers:
  if i == 1:
    continue
  for j in range(2,int(i**0.5 + 1)):
    if i % j == 0:
      break
  else:
    count += 1
print(count)