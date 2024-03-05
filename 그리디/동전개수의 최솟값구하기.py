num,object = map(int,input().split())
list =[]

for i in range(num):
  a = int(input())
  list.append(a)

count = 0

# for i in list:
#   if object==0:
#     print(count)
#     break
#   if i <= object:
#     count += object // i
#     object = object % i

for i in range(num-1 , -1, -1):
  if list[i] <= object:
    count += object//list[i]
    object = object % list[i]
print(count)

