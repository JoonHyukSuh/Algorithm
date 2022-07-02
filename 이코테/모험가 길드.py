#모험가 길드
N = int(input())
level = list(map(int,input().split()))
level.sort(reverse=True)
group = 0
while True:
  del level[:level[0]]
  group += 1
  if len(level) == 0:
    break
print(group)