#1018 체스판 다시 칠하기 
n, m = map(int,input().split())
graph = [list(input()) for _ in range(n)]

result = []

for i in range(0,n-7):
  for j in range(0,m-7):
    w_cnt = 0
    b_cnt = 0
    for x in range(i,i+8):
      for y in range(j,j+8):
        if (x+y) % 2 == 0:
          if graph[x][y] != 'W':
            w_cnt += 1
          if graph[x][y] != 'B':
            b_cnt += 1 
        else:
          if graph[x][y] != 'W':
            b_cnt += 1
          if graph[x][y] != 'B':
            w_cnt += 1
    result.append(w_cnt)
    result.append(b_cnt)
print(min(result))