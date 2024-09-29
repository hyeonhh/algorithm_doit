# 필요한 변수
# n* m 방
n,m = map(int,input().split())
clean_count = 1


dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 현재 위치 
x,y,d = map(int,input().split())
room = []

# 방 구조 정보 입력
for _ in range(n):
    room.append(list(map(int,input().split())))

room[x][y] = 2
while True:
    flag = 0
    for _ in range(4):
        d = (d+3)% 4
        nx = x + dx[d]
        ny = y + dy[d]

        # 범위 안에 들고, 빈칸이고, 청소할 수 있다면
        # 반시계 방향으로 돌리고, 카운트하고, 현재 위치를 갱신하고, flag변경
        if 0 <= nx <n and 0 <= ny <m and room[nx][ny] == 0:
            clean_count +=1
            x = nx
            y = ny
            room[x][y] = 2
            flag = 1
            break

    if flag == 0:
        # 모두 청소를 할 수 없을 때 
        # 벽이라면
        if room[x-dx[d]][y-dy[d]] == 1:
            print(clean_count)
            break
    # 뒤가 벽이 아니라면
        else:
            x, y = x-dx[d], y-dy[d]