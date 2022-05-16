a,b = map(int,input().split())
new_a = str(a)
new_a = int(new_a[::-1])
new_b = str(b)
new_b = int(new_b[::-1])

if new_a > new_b:
    print(new_a)
else:
    print(new_b)

    


