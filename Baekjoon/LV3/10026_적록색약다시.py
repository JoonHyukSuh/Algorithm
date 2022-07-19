#10026 적록색약 -BFS
from collections import deque 
n = int(input())
graph = [list(input()) for _ in range(n)]
visted =[[False]*n for _ in range(n)]

def bfs(x,y):
    visted[x][y]=1
    queue = deque()
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0<=nx<n) and (0<=ny<n):
                if graph[nx][ny] == graph[x][y] and visted[nx][ny]==False:
                    visted[nx][ny]=True
                    queue.append([nx,ny])



dx = [1,-1,0,0]
dy = [0,0,1,-1]

r,g,b = 0,0,0
for i in range(n):
    for j in range(n):
        if visted[i][j]==0:
            bfs(i,j)
            if graph[i][j]=='R':
                r += 1 
            elif graph[i][j]=='G':
                g += 1
            else:
                b += 1
                 
cnt1 = r+g+b
              

for i in range(n):
    for j in range(n):
        if graph[i][j]=='G':
            graph[i][j]='R'



visted =[[False]*n for _ in range(n)]
r1,b1 = 0,0 
for i in range(n):
    for j in range(n):
        if visted[i][j]==0:
            bfs(i,j)
            if graph[i][j]=='R':
                r1 += 1
            else:
                b1 +=1
                
cnt2 = r1 + b1 

print(cnt1,cnt2)