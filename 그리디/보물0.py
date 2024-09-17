n = int(input())

a = list(map(int,input().split())) # 1 1 1 6 0 
b = list(map(int,input().split())) # 2 7 8 3 1 
total = 0 

# 합
while True:
    total += min(a) * max(b)
    a.remove(min(a))
    b.remove((max(b)))
    if len(a)==0:
        break

print(total)
