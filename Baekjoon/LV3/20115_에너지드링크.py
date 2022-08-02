#20115 에너지 드링크 
n = int(input())
amt = sorted(list(map(int,input().split())),reverse = True)
cnt = amt[0]

for i in range(n-1):
  cnt += amt[1]/2
  amt.pop(1)

print(cnt)