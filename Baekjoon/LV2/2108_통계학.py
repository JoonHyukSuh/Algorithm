#통계학

n = int(input())
num_list = []
num_dict = {}
for _ in range(n):
  num = int(input())
  num_list.append(num)
  if num not in num_dict:
    num_dict[num] = 1
  else:
    num_dict[num] += 1
num_list.sort()
avg = int(round(sum(num_list) / n,0))

med = num_list[len(num_list)//2]

mode_val = max(num_dict.values())
mode_list = []
for key, val in num_dict.items():
  if val == mode_val:
    mode_list.append(key)
if len(mode_list) == 1:
  mode = mode_list[0]
else:
  mode_list.sort()
  mode = mode_list[1]
range_ = max(num_list) - min(num_list)

print(avg)
print(med)
print(mode)
print(range_) 