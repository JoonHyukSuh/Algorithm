#20207 달력 
n = int(input())
calendar = [0 for _ in range(366)]
schedule_list = []
total = 0
length, width = 0,0 
for _ in range(n):
  start, end = map(int,input().split())
  schedule = []
  for i in range(start,end+1):  
    schedule.append(i)
    calendar[i] += 1 
  schedule_list.append(schedule)

for i in range(1,366):
  if calendar[i] != 0:
    length = max(length,calendar[i])
    width += 1
    if i == 365:
      total += length*width    
  else:
    total += length*width
    length, width = 0, 0
print(total)