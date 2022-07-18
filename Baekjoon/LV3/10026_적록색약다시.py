from collections import deque 

N = int(input())
arr = [list(input()) for _ in range(N)]
visted =[[0]*N for _ in range(N)]


def bfs(x,y):
    visted[x][y]=1
    d = deque()
    d.append([x,y])
    while d:
        x,y = d.popleft()
        flag = arr[x][y]
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if (0<=a<N) and (0<=b<N):
                if arr[a][b] == flag and visted[a][b]==0:
                    visted[a][b]=1
                    d.append([a,b])



dx = [1,-1,0,0]
dy = [0,0,1,-1]
r_cnt,g_cnt,b_cnt = 0,0,0
for i in range(N):
    for j in range(N):
        if visted[i][j]==0:
            bfs(i,j)
            if arr[i][j]=='R':
                r_cnt+=1
            elif arr[i][j]=='G':
                g_cnt+=1
            else:
                b_cnt+=1
                 
cnt1 = r_cnt+g_cnt+b_cnt
              

for i in range(N):
    for j in range(N):
        if arr[i][j]=='G':
            arr[i][j]='R'



visted =[[0]*N for _ in range(N)]
r_cnt,b_cnt = 0,0
for i in range(N):
    for j in range(N):
        if visted[i][j]==0:
            bfs(i,j)
            if arr[i][j]=='R':
                r_cnt+=1
            else:
                b_cnt+=1
                
cnt2 = r_cnt+b_cnt

print(cnt1,cnt2)