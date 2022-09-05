#11047 동전0
n, k = map(int,input().split())
nums = []
for _ in range(n):
  nums.append(int(input()))
nums.sort(reverse = True)
cnt = 0
for i in nums:
  if k == 0:
    break
  cnt += k // i
  k %= i 
print(cnt)