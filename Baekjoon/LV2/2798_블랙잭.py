#2798 블랙잭
from itertools import combinations
import heapq
n,m = map(int,input().split())
nums = map(int,input().split())

combination = combinations(nums,3)
heap = []
for i in combination:
  if sum(i) <= m:
    heapq.heappush(heap,(m-sum(i),sum(i)))
print(heapq.heappop(heap)[1]) 