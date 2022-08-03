#10989 수 정렬하기 3
import sys
import heapq
#input = sys.stdin.readline

n = int(input())
num_list = [0 for _ in range(10001)]

for _ in range(n):
  num_list[int(input())] += 1

for i in range(len(num_list)):
  if num_list[i] != 0:
    for j in range(num_list[i]):
      print(i)