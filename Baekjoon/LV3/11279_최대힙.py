#11279 최대 힙 - 2주차 공통문제
import heapq
import sys 
n = int(input())
heap = []
for _ in range(n):
  nums = int(sys.stdin.readline())
  if nums > 0:
    heapq.heappush(heap,-nums)
  else:
    if len(heap) == 0: 
      print(0)
    else:
      print(-heapq.heappop(heap))