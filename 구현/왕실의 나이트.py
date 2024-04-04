position = input()

# 좌표로 변환
# -> 딕셔너리로 구현해보기

col = {'a':1,'b':2, 'c': 3,'d':4 , 'e':5,'f':6,'g':7,'h':8}



x =  int(position[1])
y = col[position[0]]


count =0

# 이동 로직 2
steps =[(-2,1), (-1,2), (1,2) , (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)] 


for i in steps:
  nx = x + i[0]
  ny = y + i[1]
  if nx<1 or ny<1 or nx>8 or ny>8:
    continue
  else:
    count +=1
print(count)