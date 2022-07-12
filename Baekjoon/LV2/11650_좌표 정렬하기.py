#11650 좌표 정렬하기
n = int(input())
c= sorted([list(map(int,input().split())) for _ in range(n)], key = lambda x:(x[0], x[1]))
for i in c:
  print(i[0],i[1])
