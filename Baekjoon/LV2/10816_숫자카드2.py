#10816 숫자카드2
import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))

m = int(input())
cards = list(map(int,input().split()))

cnt_list = []

for i in cards:
  cnt = 0
  for j in range(len(nums)):
    if i == nums[j]:
      cnt += 1
  cnt_list.append(cnt)


for i in cnt_list:
  print(i,end=" ")