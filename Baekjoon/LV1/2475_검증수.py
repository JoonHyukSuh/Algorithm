num = input().split()
num_list = list(map(int,num))
new_list = []
for i in num_list:
    i = i**2
    new_list.append(i)
total = sum(new_list)
answer = total % 10
print(answer)