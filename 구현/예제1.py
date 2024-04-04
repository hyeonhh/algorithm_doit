n = int(input())
list = input().split()

# 현재 위치
x,y=1,1

dx = [0,0,-1,1]
dy =[-1,1,0,0]

move_types =["L","R","U","D"]

for i in list:
  for j in range(4):
    if i ==move_types[j]:
      nx = x+dx[j]
      ny = y+dy[j]
  if nx <1 or ny<1 or nx>n or ny >n :
    continue
  x,y = nx,ny
      
print(x,y)
