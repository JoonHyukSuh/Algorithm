num = input().split()
num_list = list(map(int,num))
for i in num_list:
    i = i*i
total = sum(num_list)
answer = total % 10
print(answer) 