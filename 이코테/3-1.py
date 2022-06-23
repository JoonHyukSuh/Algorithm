n = 1260
count = 0

types = [500,100,50,10]
for coin in types:
    count += n
    n %= coin

print(coin)