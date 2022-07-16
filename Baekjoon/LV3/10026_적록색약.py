#10026 적록색약
# 일반인, 적록색약일 때 함수 두 개 나눠서 
import sys
sys.setrecursionlimit(10001)
n = int(input())
graph = [list(map(str,input().rstrip())) for _ in range(n)]
rg_graph = graph 

#상하좌우 
dx = [-1,1,0,0] 
dy = [0,0,-1,1]

visited = [[False] * n for _ in range(n)]
result = 0
rg_visited = [[False] * n for _ in range(n)]
rg_result = 0 

#일반인
def dfs(x,y):
  if x <= -1 or x >= n or y <= -1 or y>= n:
    return False
  visited[x][y] == True
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0<= ny < n:
      if graph[nx][ny] == graph[x][y] and visited[nx][ny] == False:
        dfs(nx,ny)
#적록색약
def rg_dfs(x,y):
  if x <= -1 or x >= n or y <= -1 or y>= n:
    return False
  rg_visited[x][y] == True 
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0<= ny < n:
      if rg_graph[nx][ny] == rg_graph[x][y] and rg_visited[nx][ny] == False:
        rg_dfs(nx,ny)

#일반인 
for i in range(n):
  for j in range(n):
    if visited[i][j] == False:
      dfs(i,j)
      result += 1

#적록색약 
for i in range(n):
  for j in range(n):
    if rg_graph[i][j] == 'R':
      rg_graph[i][j] == 'G'
    if rg_visited[i][j] == False:
      rg_dfs(i,j)
      rg_result += 1 

print(result, rg_result)




