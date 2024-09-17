n, k = map(int,input().split())
count = 0

if (n%k!=0):
    count = 1 *(n%k)
    n = k * (n//k)

while n>=k:
    count +=1
    n //=k
    if n==1:
        break
print(count) 