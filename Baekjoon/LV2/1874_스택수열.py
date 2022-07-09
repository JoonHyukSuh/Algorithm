#1874 스택수열
n = int(input())
stack = []
result = []
temp = True
cnt = 1 
for _ in range(1,n+1):
  num = int(input())
  while cnt <= num:
    stack.append(cnt)
    result.append('+')
    cnt += 1
  if stack[-1] == num:
    stack.pop()
    result.append('-')
  else:
    temp = False

if temp == False:
  print('NO')
else :
  for i in result:
    print(i)