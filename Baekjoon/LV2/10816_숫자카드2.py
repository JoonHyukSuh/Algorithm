#10816 숫자카드2
import sys
from collections import defaultdict
#input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))
m = int(input())
cards = list(map(int,input().split()))

ans = defaultdict(int)

for i in nums:
  ans[i] += 1

for i in cards:
  if i in ans:
    print(ans[i],end=' ')
  else:
    print(0,end=' ')