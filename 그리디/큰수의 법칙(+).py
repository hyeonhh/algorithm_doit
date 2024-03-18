n,m,k = map(int,input().split())
list = list(map(int,input().split()))

list.sort()
first = list[n-1]
second = list[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = 0
count += m//(k+1) * k +( m %(k+1))

sum=0
sum += count *first
sum +=( m-count) *second

print(sum)
