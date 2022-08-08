#1764 듣보잡 
n,m = map(int,input().split())
listen = []
see = []

for _ in range(n):
  x = input()
  listen.append(x)

for _ in range(m):
  y = input()
  see.append(y)

answer = list(set(listen) & set(see))
answer.sort()
print(len(answer))
for i in answer:
  print(i)