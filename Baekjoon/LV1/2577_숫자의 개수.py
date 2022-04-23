num_list = []
for i in range(3):
    num_list.append(int(input()))
mult = 1 
for i in num_list:
    mult = mult * i
answer = str(mult)
count = 0
for i in answer:
    if i == 