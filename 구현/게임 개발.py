n, m = map(int,input().split())
x,y,direction = map(int,input().split())



#전체 맵 정보
entire_map = []
for i in range(n):
  entire_map.append(list(map(int,input().split())))

# 이동 시 좌표 변화
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 경우의 수 
count = 1

# 몇 번 회전했는지 
turn_time =0

# 왼쪽으로 방향 회전 함수
def turn_left():
  global direction
  direction-=1
  if direction == -1:
    direction = 3

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if nx>0 and ny>0 and entire_map[nx][ny] == 0:
      count += 1
      entire_map[nx][ny] = 1
      x =nx
      y = ny
      turn_time = 0
      continue
    else:
      turn_time +=1

    # 중단 조건 
    if turn_time ==4:
      nx = x - dx[direction]
      ny = y - dy[direction]
      if entire_map[nx][ny] ==0:
        x = nx
        y = ny
      else:
        break
      turn_time = 0
      
print(count)