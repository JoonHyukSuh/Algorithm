#10026 적록색약 -BFS
from collections import deque
n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
rg_graph = graph

visited = [[False] * n for _ in range(n)]
rg_visited = [[False] * n for _ in range(n)]

#상하좌우 
dx = [-1,1,0,0] 
dy = [0,0,-1,1]

result = 0 
rg_result = 0 
def bfs(x,y):
  visited[x][y] = True
  queue = deque()
  queue.append([x,y])
  if x <= -1 or x >= n or y <= -1 or y>= n:
    return False
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0<= ny < n:
        if graph[nx][ny] == graph[x][y] and visited[nx][ny] == False:
          visited[nx][ny] = True #인접한 색이 같을 경우
          queue.append([nx,ny])

def rg_bfs(x,y):
  rg_visited[x][y] = True
  rg_queue = deque()
  rg_queue.append([x,y])
  if x <= -1 or x >= n or y <= -1 or y>= n:
    return False
  while rg_queue:
    x,y = rg_queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0<=ny<n:
        if rg_graph[nx][ny] == rg_graph[x][y] and rg_visited[nx][ny] == False:
          rg_visited[nx][ny] = True
          rg_queue.append([nx,ny])

for i in range(n):
  for j in range(n):
    if visited[i][j] == False:
      bfs(i,j)
      result += 1 

for i in range(n):
  for j in range(n):
    if rg_graph[i][j] == 'R':
      rg_graph[i][j] == 'G'
    if rg_visited[i][j] == False:
      rg_bfs(i,j)
      rg_result += 1

print(result, rg_result)


        