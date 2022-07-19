#1012 유기농배추
from collections import deque  
T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0 

def bfs(x,y):
  graph[x][y] = 0
  queue = deque()
  queue.append([x,y])
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        queue.append([nx,ny])
  return 

for i in range(T):
  cnt = 0 
  n,m,k = map(int,input().split())
  graph = [[0]*m for _ in range(n)]

  for j in range(k):
    x,y = map(int,input().split())
    graph[x][y] = 1

  for x in range(n):
    for y in range(m):
      if graph[x][y] == 1:
        bfs(x,y)
        cnt += 1 
  print(cnt)
