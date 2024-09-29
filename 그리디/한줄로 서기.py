# 입력
n = int(input())
left_list = list(map(int,input().split()))
height_list = [0] * n

# 키 
for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == left_list[i] and height_list[j] == 0:
            height_list[j] = i+1
            break
        elif height_list[j]==0:
            cnt +=1


# 출력
print(" ".join(map(str,height_list)))
