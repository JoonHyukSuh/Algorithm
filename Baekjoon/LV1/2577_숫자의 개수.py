a = int(input())
b = int(input())
c = int(input())
mult = a * b * c
answer = list(str(mult))
for i in range(10):
    print(answer.count(str(i)))