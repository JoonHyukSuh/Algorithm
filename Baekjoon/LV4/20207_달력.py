#20207 달력 
n = int(input())
schedule = [list(map(int,input().split())) for _ in range(n)]

total = 0
height = 0
length = 0
for i in range(len(schedule)-1):
    i 