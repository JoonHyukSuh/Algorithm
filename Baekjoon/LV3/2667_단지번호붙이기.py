#2667 단지번호붙이기
from collections import deque 
n = int(input())
graph = [list(map(int,input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  graph[x][y] = 0
  queue = deque()
  queue.append([x,y])
  cnt = 1 
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        queue.append([nx,ny])
        cnt += 1
  return cnt 

cnt_list = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      cnt_list.append(bfs(i,j))
       
cnt_list.sort()
print(len(cnt_list))
for i in range(len(cnt_list)):
  print(cnt_list[i])
