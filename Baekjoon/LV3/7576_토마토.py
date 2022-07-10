#7576 토마토 - 스터디 공통 문제 - bfs 
from collections import deque
m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)] #정보를 2차원 리스트에 저장
queue = deque()

dx = [-1,1,0,0] #상하좌우
dy = [0,0,-1,1] #상하좌우 

for i in range(n): #n행동안 
  for j in range(m): #m열동안 
    if graph[i][j] == 1: #익은 토마토가 있으면 
      queue.append(([i,j])) #큐에 저장하자 
      
def bfs():
  while queue: #큐를 돌 동안 
    x,y = queue.popleft() #익은 토마토 pop 
    for i in range(4): #4가지 방향 탐색 
      nx = x + dx[i] 
      ny = y + dy[i]
      if 0 <= nx < n  and 0 <= ny < m and graph[nx][ny] == 0: #범위 안에 있고 아직 익지 않은 토마토라면 
        graph[nx][ny] = graph[x][y] + 1 #1을 더해주며 횟수 세기, main idea
        queue.append([nx,ny]) #queue에 익은 토마토 좌표 추가 
bfs() # bfs 함수 돌며 최종 익은 토마토 구하기 

result = 0
ripen = True #모두 익었다는 전제 

for i in graph: # i 행 j 열 돌 동안 
  for j in i:
    if j == 0: #익지 않은 것이 있으면 
      ripen = False #ripen은 False 
    result = max(result, j) #결과는 최대횟수에서 -1 

if ripen == False: #익지 않은게 있으면 -1 
  print(-1)
else:
  print(result-1) #결과에서 -1 