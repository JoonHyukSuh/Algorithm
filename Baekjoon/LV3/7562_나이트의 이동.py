#7562 나이트의 이동
from collections import deque 
t = int(input())

dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,-2,-1,1,2]

def bfs(x,y):
  queue = deque()
  queue.append([x,y])
  while queue:
    x,y = queue.popleft()
    if x == target_x and y == target_y:
      print(graph[x][y])
      break
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] == 0:
          graph[nx][ny] = graph[x][y] + 1
          queue.append([nx,ny])

for _ in range(t):
  n = int(input())
  graph = [[0]*n for _ in range(n)]
  x,y = map(int,input().split())
  target_x , target_y = map(int,input().split())
  bfs(x,y)