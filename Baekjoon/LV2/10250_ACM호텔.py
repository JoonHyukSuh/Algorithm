#10250 ACM호텔
t = int(input())
for i in range(t):
  h,w,n = map(int,input().split())
  floor = n % h 
  room = n // h + 1
  if n % h ==0:
    floor = h
    room = n // h
  print(f'{floor*100+room}')
