#10871 x보다 작은 수
n , x = map(int,input().split()) #n,x입력 
a = list(map(int,input().split())) #수열 a 입력, 리스트로 저장 
for i in a: #리스트 a 에서
  if i < x: # x 보다 작은게 있으면 
    print(i,end=' ') # 출력 