#11286 절대값 힙 - 2주차 공통문제
import heapq
import sys 
n = int(input())
heap = []
for _ in range(n):
  nums = int(sys.stdin.readline())
  if nums != 0:
    heapq.heappush(heap,(abs(nums),nums))  
  else:
    if len(heap) == 0:
      print(0)
    else:
      print(heapq.heappop(heap)[1]) #힙의 인덱스를 출력