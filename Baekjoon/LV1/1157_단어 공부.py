example = input().upper()

keys = list(set(example))
cnt = []
for i in keys:
    cnt.append(example.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(keys[cnt.index(max(cnt))])