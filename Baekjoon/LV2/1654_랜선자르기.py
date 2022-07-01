k,n = map(int,input().split())
k_list = []
for _ in range(k):
    k_length = int(input())
    k_list.append(k_length)
upper, lower = max(k_list), 1
while lower <= upper:
  cnt = 0
  for i in k_list:
    avg = (upper + lower) // 2
    cnt += i // avg
  if cnt >= n :
    lower = avg + 1 
    answer = avg
  elif cnt < n :
    upper = avg - 1
print(answer)
