#2609 최대공약수와 최소공배수
n,m = map(int,input().split())
def gcd(n,m):
  r = m % n
  if r != 0:
    m,n = n, r
    return gcd(n,m)
  else:
    return n 
print(gcd(n,m))
print(int(m*n/gcd(n,m)))