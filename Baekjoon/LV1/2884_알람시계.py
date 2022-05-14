h, m = map(int,input().split())
if m >= 45:
    new_m = m - 45
    new_h = h
else:
    new_m = m + 15
    if h !=0:
        new_h = h-1
    else:
        new_h = h+23
print(new_h,new_m)

