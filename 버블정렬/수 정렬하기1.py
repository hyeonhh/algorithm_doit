num = int(input())
list=[]


for i in range(num):
  sort_num = int(input())
  list.append(sort_num)


for j in range(num,1,-1):
  for i in range(j-1):
    # list[i]와 list[i+1]을 비교
    if list[i] > list[i+1]:
      temp = list[i]
      list[i] = list[i+1]
      list[i+1] = temp
    
for i in list:
  print(i) 