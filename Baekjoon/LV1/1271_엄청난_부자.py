#1271 엄청난 부자
n , m = map(int,input().split())

money = n // m 
rest = n - m*money 
print(money)
print(rest) 
