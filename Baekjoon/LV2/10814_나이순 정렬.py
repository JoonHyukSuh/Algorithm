#10814 나이순 정렬 
import heapq
n = int(input())
heap = []
output = []
for i in range(n):
  age, name = input().split()
  heapq.heappush(heap,(int(age),i,name))

for i in range(n):
  output.append(heapq.heappop(heap))
  print(output[i][0],output[i][2])