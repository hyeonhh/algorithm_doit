n,m = map(int,input().split())
pocket = []
for i in range(n):
    pocket.append(i+1)

for _ in range(m):
    i,j = map(int,input().split())
    pocket[i-1:j] =  pocket[i-1:j][::-1]

print(pocket)

for x in range(n):
    print(pocket[x], end=" ")
