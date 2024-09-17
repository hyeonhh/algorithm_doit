n = int(input())
time_list = list(map(int,input().split()))

time_list.sort()
print(time_list)

# 누적합 구하기 
time_sum_list = [0] * n
for i in range(n):
    if (i==0):
        time_sum_list[0] = time_list[0]
    else :
        time_sum_list[i] = time_sum_list[i-1] + time_list[i]

# 0번째 사람:  0번째
# 1번째 사람:  0번째 사람 소요 시간 + 본인 시간 = 0 +1
# 2번째 사람 :  1번째 사람 소요 시간 + 본인 시간 = 0 + 1 + 2 번째 사람
# 3번째 사람은 2번째 사람 소요 시간 + 본인 시간  =2번째 총 소요시간  + 3번째 시간
# 4번째 사람은 3번째 사람 소요 시간 + 본인 시간  = 1 + 2 + 3 + 4

print(sum(time_sum_list))
