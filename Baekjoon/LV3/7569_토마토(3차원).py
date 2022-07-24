#7569 토마토 - 3차원
from collections import deque
m,n,h = map(int,input().split())
graph = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k] == 1:
        queue.append([i,j,k])

def bfs():
  while queue:
    z,x,y = queue.popleft()
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]

      if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
        if graph[nz][nx][ny] == 0:
          graph[nz][nx][ny] = graph[z][x][y] + 1 
          queue.append([nz,nx,ny])



bfs()

ripen = True
result = -1 

for i in graph:
  for j in i:
    for k in j:
      if k == 0:
        ripen = False
      result = max(result,k)


if ripen == False:
  print(-1)
elif result == 1:
  print(0)
else:
  print(result-1)