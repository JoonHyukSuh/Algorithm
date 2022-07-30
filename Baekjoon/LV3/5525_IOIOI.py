#5525 IOIOI 'IOI'를 한 묶음으로 
n = int(input())
m = int(input())
s = input().strip()

i_index = [i for i in range(m) if s[i] == 'I']
cnt = 0
target = n
answer = 0
for i in range(1,len(i_index)):
  if i_index[i] - i_index[i-1] ==2:
    cnt += 1
  else:
    cnt = 0
  if cnt >= target:
    answer += 1
print(answer)
#[2,4,6,8,9,11,12]