#11651 좌표 정렬하기 2
import heapq
n = int(input())
heap = []
output = []
for _ in range(n):
  x,y = map(int,input().split())
  heapq.heappush(heap,(y,x))
for i in range(n):
  output.append(heapq.heappop(heap))
  print(output[i][1], output[i][0])
