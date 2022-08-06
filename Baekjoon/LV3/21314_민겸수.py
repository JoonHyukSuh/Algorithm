#21314 민겸수
#mk든,mm이든,kk든 자리수는 똑같음
#최대 => mk최대한 붙여놓기, mm떨어뜨려놓기 최소 => ㅡmm끼리는 최대한 붙여놓고, k는 떨어뜨려놓기
mk = input()
max_mk = ''
min_mk = ''
cnt = 0
for i in mk:
  if i == 'M': #MM인경우
    cnt += 1
  else: #MK인 경우
    if cnt > 0:
      min_mk += '1'+'0'*(cnt-1) + '5'
      max_mk += '5'+'0'*(cnt)
    else: # KK 인경우
      min_mk += '5'
      max_mk += '5'
    cnt = 0

if cnt > 0: #K 나온 이후 M붙어있을때 
  min_mk += '1'+'0'*(cnt-1)
  max_mk += '1' *cnt

print(max_mk, min_mk)