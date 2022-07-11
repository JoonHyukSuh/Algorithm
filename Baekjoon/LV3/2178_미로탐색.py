#2178 미로 탐색 
from collections import deque 
n,m = map(int,input().split()) #n행 m열 입력받음 
graph = [list(map(int,input())) for _ in range(n)] #graph 정보 2차원 리스트 저장 

#상하좌우 
dx = [-1,1,0,0] 
dy = [0,0,-1,1]

def bfs(x,y):
  queue = deque() 
  queue.append([x,y]) #첫 좌표 queue에 저장 (0,0)
  while queue:
    x,y = queue.popleft() #첫 좌표 popleft 
    for i in range(4): # 상하좌우 탐색 
      nx = x + dx[i] #새로운 좌표 
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m: #범위를 벗어나는 경우 
        continue 
      if graph[nx][ny] == 0: # 이동이 안되는 경우 
        continue
      if graph[nx][ny] == 1: # 이동할 수 있는 경우 
        graph[nx][ny] = graph[x][y] + 1 #다음 노드 +1 :토마토 문제와 같은 아이디어 
        queue.append([nx,ny]) #새로운 좌표에 추가한다 
  return graph[n-1][m-1] #거리는 -1이므로 
print(bfs(0,0))

