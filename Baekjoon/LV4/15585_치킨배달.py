#15686 치킨 배달 -- bfs 말고 combinations
from itertools import combinations 
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
bbq = []
home = []

for i in range(n):
  for j in range(n):
    if graph[i][j] == 2:
      bbq.append([i,j])

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      home.append([i,j])

chicken_list= list(combinations(bbq,m))

def c_distance(home,bbq):
  min_dist = 99999920220726
  for i in bbq:
    dist = abs(i[0] - home[0]) + abs(i[1] - home[1])
    min_dist = min(min_dist,dist)
  return min_dist

chicken_distance = []
for i in chicken_list:
  distance = 0
  for j in home:
    distance += c_distance(j,i)
  chicken_distance.append(distance)

print(min(chicken_distance))