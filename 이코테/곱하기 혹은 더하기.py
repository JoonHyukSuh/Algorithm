#곱하기 혹은 더하기
S = str(input())
sum = int(S[0])
for i in range(len(S)-1):
  if S[i] != '0' and S[i+1] != '0':
    sum *= int(S[i+1])
  elif S[i] =='0' or S[i+1] == '0':
    sum += int(S[i+1])
print(sum) 
