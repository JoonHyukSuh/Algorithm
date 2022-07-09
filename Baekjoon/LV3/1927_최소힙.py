#1927 최소 힙
import heapq
import sys 
n = int(input())
heap = []
for _ in range(n):
  info = int(sys.stdin.readline())
  if info != 0:
    heapq.heappush(heap,info)
  else:
    if len(heap) == 0:
      print(0)
    else:
      print(heapq.heappop(heap))