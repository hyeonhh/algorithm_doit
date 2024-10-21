import sys
sys.setrecursionlimit(10000)
# 입력
test_case_num = int(input())


def dfs(x,y):
    global visited,cavarage
    if x<0 or x>=n or y<0 or y>=m:
        return
    elif visited[x][y] or cavarage[x][y]==0:
       return 
   
   # visited가 True인지 False인지는 visited[x][y] 그리고 not visited[x][y]으로 작성 가능
    elif not visited[x][y] and cavarage[x][y] ==1:
        visited[x][y] = True
        # 상하좌우 방향으로 조사하기
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)   
        
                     
        
for _ in range(test_case_num): 
    m,n,k = map(int,input().split())
    result = 0

    # 방문 리스트
    visited = [[False] * m  for _ in range(n)]    
    # 배추 리스트
    cavarage = [ [0] * m for _ in range(n)]
    
    for _ in range(k): 
           # 배추가 있는 위치
        cavarage_x,cavarage_y = map(int,input().split())
        cavarage[cavarage_y][cavarage_x] = 1
    for  i in range(n):
        for j in range(m):   
            if cavarage[i][j] == 1 and not visited[i][j]:
                dfs(i,j)
                
                # 상하 좌우 확인 모두가 끝나면 result를 1 증가시켜주면 된다.
                result +=1   
    # 1번의 테스트 케이스가 끝나면 결과를 출력해야한다.
    print(result)     
        
    
    
        