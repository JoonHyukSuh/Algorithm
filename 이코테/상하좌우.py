########구현##########
#상하좌우
N = int(input())
x,y = 1,1
plan = input().split()
#이동방향 좌우상하 
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','P']

#이동 계획 하나씩 확인
for i in plan:
  #이동 후 좌표 구하기
  for j in range(len(move_types)):
    if i == move_types[j]:
      nx = x + dx[j]
      ny = y + dy[j]
  #공간 벗어나는 경우
  if nx < 1 or ny < 1 or nx > N or ny > N:
    continue
  # 이동 수행 
  x,y = nx, ny
print(x,y)