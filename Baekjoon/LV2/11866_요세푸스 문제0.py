#11866 요세푸스 문제 0
from collections import deque 
n, k = map(int,input().split())
people = deque([i for i in range(1,n+1)])
new = []
for _ in range(len(people)):
  people.rotate(-(k-1))
  new.append(people.popleft())
print('<',end='')
for i in new:
  if i == new[-1]:
    print(i,end='')
  else:
    print(i,end=', ')
print('>')