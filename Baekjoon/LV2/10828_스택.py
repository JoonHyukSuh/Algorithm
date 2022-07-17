#10828 스택
import sys
input = sys.stdin.readline
n = int(input())
n_list = []
for _ in range(n):
  cmd = input().split()
  if cmd[0] == 'push':
    n_list.append(int(cmd[1]))
  elif cmd[0] == 'pop':
    if len(n_list) == 0:
      print(-1)
    else:
        print(n_list.pop())
  elif cmd[0] =='size':
    print(len(n_list))
  elif cmd[0] == 'empty':
    if len(n_list) == 0:
      print(1)
    else:
      print(0)
  elif cmd[0] == 'top':
    if len(n_list) == 0:
      print(-1)
    else:
      print(n_list[-1])
