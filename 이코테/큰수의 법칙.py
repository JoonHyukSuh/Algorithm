#큰수의 법칙
n,m,k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
largest = data[0]
second_largest = data[1]
sum = 0
while True:
  for i in range(k):
    if m == 0:
      break
    sum += largest
    m -= 1
  if m == 0:
    break
  result += second_largest
  m -= 1 
print(sum)

    