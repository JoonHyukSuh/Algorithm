#15787 기차가 어둠을 헤치고 은하수를
from collections import deque
n, m = map(int,input().split())
seats = [deque([0 for _ in range(20)]) for _ in range(n)] #처음엔 모든 기차 자리 비워둠
record = []

for _ in range(m):
  cmd = list(map(int,input().split()))
  if cmd[0] == 1: #1번 명령
    seats[cmd[1]-1][cmd[2]-1] = 1 #i번째기차 (기차번호1번부터시작), x좌석 채우기
  elif cmd[0] == 2:
    seats[cmd[1]-1][cmd[2]-1] = 0 #i번째기차 (기차번호1번부터시작), x좌석 비우기
  elif cmd[0] == 3:
    seats[cmd[1]-1].rotate(1) #뒤로 한칸씩 이동, 사람 있으면 첫자리는 초기화
    seats[cmd[1]-1][0] = 0
  elif cmd[0] == 4:
    seats[cmd[1]-1].rotate(-1) #앞으로 한칸씩 이동, 사람 있으면 뒷자리는 초기화
    seats[cmd[1]-1][-1] = 0

for i in seats:
  if i not in record:
    record.append(i)

print(len(record))