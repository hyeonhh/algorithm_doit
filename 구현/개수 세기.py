# 정수의 개수
n = int(input())

# 정수 리스트
n_list = list(map(int,input().split()))


# 찾으려는 정수 
v = int(input())

# 정수 개수
count = 0

for i in n_list:
    if i == v:
        count+=1
    else:
        continue


print(count)
