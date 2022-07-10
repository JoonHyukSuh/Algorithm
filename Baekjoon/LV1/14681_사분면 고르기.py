#14681 사분면 고르기
x = int(input()) 
y = int(input())
if x > 0 and y > 0 : #모두 양수일 때: 1사분면 
  print(1)
elif x > 0 and y < 0 : #x는 양수, y는 음수일 때
  print(4)
elif x < 0 and y > 0 : #x는 음수, y는 양수일 때 
  print(2)
else: # 그 외: 3사분면 
  print(3)