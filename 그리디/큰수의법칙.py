n,m,k = map(int,input().split())

list = list(map(int, input().split()))
list.sort(reverse=True)

max = list[0]
second = list[1]
sum = 0
count=0

while True:
  for _ in range(k):
    if count == m:
      break
    sum +=max
    count += 1
  sum += second
  count +=1
  if count ==m:
    break
print(sum)
