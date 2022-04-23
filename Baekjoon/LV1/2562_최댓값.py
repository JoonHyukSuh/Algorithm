num = []
for i in range(9):
    num.append(int(input()))
for i in range(len(num)):
    if num[i] == max(num):
        print(num[i])
        print(i+1)
