num_list = []
for i in range(3):
    num_list.append(int(input()))
mult = 1 
for i in num_list:
    mult = mult * i
answer = str(mult)
ans_list = []
for i in answer:
    a = string.count(i)
    ans_list.append(a)
