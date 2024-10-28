n = int(input())


house = []
# 집 정보 리스트
for _ in range(n): 
    house.append(list(map(int,input())))

# 방문 리스트
visited = [[False] * n for _ in range(n)]

# 상하 좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 집 수 
house_count = 0

# 단지 수 
count = 0

# 단지 별 각 집의 수를 넣을 리스트
house_list = []

def dfs(x,y): 
    global house, house_count, count, visited
    # 범위 밖으로 이동 시 리턴 
    if x >= n or x < 0 or y >= n or y < 0: 
        return 
    # 이미 검사한 집이라면 건너뛰기
    if visited[x][y]:
        return 
    
    # 만약 현재 인덱스가 집이라면? 다른 집이 주변에 더 있는지 찾아봐야한다.
    if not visited[x][y] and house[x][y] == 1:
        house_count += 1
        visited[x][y] = True 

    # 상하 좌우 검사
    for i in range(4): 
        new_x = dx[i] + x
        new_y = dy[i] + y
        dfs(new_x, new_y)
			   
for i in range(n): 
    for j in range(n): 
        # 아직 방문하지 않았고, 집이라면 Dfs 실행한다. 
        if not visited[i][j] and house[i][j] == 1: 
            # 현재까지의 집 수를 리스트에 넣어준 후 초기화해준다.
            house_count = 0
            dfs(i,j)
            house_list.append(house_count) 
            count += 1 
				 			   
# 출력하기 
print(count)
for num in sorted(house_list): 
    print(num)