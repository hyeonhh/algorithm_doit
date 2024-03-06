num = int(input())

# time_list = [ [0] * 2] * num

time_list = [ [0] * 2 for _ in range(num) ]

for i in range(num):
  S, E = map(int,input().split())
  time_list[i][0] = E  # 종료 시간을 기준으로 정렬해주기 위함
  time_list[i][1] = S

time_list.sort()
current = time_list[0]
count = 0
end = 0

for i in time_list:
  if  i[1] >= end: # 현재의 시간시작이 end보다 크다면
    end = i[0]
    count += 1

print(count)