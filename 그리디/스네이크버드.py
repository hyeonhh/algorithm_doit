n,l = map(int,input().split())
h_list = list(map(int,input().split()))
h_list.sort()

for i in h_list:
    if i <= l:
        l +=1
    else :
        continue

print(l)