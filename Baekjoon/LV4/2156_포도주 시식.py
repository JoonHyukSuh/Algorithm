#2156 포도주 시식
import sys
sys.setrecursionlimit(10**6)
n = int(input())
amt_list = []
for i in range(n):
  i = int(input())
  amt_list.append(i)

d = [0] * 10000

d[0] = amt_list[0]
d[1] = max(amt_list[0], amt_list[0] + amt_list[1])
d[2] = max(d[0]+amt_list[2], amt_list[1]+amt_list[2],d[1])
for i in range(2,n):
  d[i] = max(d[i-2]+amt_list[i], amt_list[i-1]+amt_list[i]+d[i-3],d[i-1])

print(max(d))