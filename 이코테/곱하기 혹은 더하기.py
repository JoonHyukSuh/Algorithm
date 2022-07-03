#곱하기 혹은 더하기
S = str(input())
sum = int(S[0])
for i in range(len(S)-1):
  if int(S[i]) > 1 and int(S[i+1]) > 1:
    sum *= int(S[i+1])
  elif int(S[i]) <=1 or int(S[i+1]) <= 1:
    sum += int(S[i+1])
print(sum) 
