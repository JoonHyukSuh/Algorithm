#1966 프린터 큐 - 스터디 공통 문제
from collections import deque
testcase = int(input())
for _ in range(testcase):
  total, location = list(map(int,input().split()))
  score = deque(map(int,input().split()))
  idx = deque(range(total)) # 순서 인덱스  
  result = 0

  while score: #스코어 돌 동안 
    if score[0] == max(score): #첫번째 원소가 최대값일 때
      result += 1 #순번에 1 추가 (첫 번째 원소가 최대이면 1)
      score.popleft() #프린트 되면 pop
      if idx.popleft() == location: #인덱스 왼쪽부터 하나씩 location이랑 같은지 확인 
        print(result) #원하는 번호(location이면 출력)
    else:
      score.append(score[0]) #뒷 순번은 마지막으로 이동
      score.popleft() #앞에 있던 뒷 순번 지우기
      idx.append(idx.popleft()) #뒷 순번의 인덱스 뒤로 이동 
