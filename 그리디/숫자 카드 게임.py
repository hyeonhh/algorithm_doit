n,m = map(int,input().split())

data =[]
result = 0

for i in range(n):
  data = list(map(int,input().split()))
  min_value = 0
  for a in data:
    min_value = min(min_value,a)
  result = max(result,min_value)
print(result)
