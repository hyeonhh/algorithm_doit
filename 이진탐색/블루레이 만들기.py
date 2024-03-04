n,m = map(int,input().split())
length = list(map(int,input().split()))

start= max(length)
end = sum(length)


# start부터 --하면서 합이 mid보다 커지면 count 1 
# 레슨의 합과 중간인덱스 값을 비교하기 

while start <= end:
  sum = 0
  count = 0
  mid = (start + end)//2

  for i in range(n):
    if sum + length[i] > mid:
      count += 1
      sum = 0
    sum += length[i]

  if sum != 0:
    count += 1
  
  if count > m:
    start = mid + 1
  else:
    end = mid - 1

   

print(start)