# 입력받기
n,m = int(input().split)
n_list=[]

for _ in range(n):
  n_list.append(int(input().split()))

# 한번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [100001] * (m+1)

# dp 구현

d[0]= 0
for i in range(n):
  for j in range(n_list[i] , m + 1):
    if d[j - n_list[i]] != 10001:
      d[j] = min( d[j], d[ j - n_list[i] ] +1)

if d[m] == 10001:
  print(-1)
else:
  print(d[m])


