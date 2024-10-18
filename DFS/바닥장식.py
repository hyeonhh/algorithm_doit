n,m = map(int,input().split())
floor_list = []
for _ in range(n):
    floor=list(input())
    floor_list.append(floor)
count = 0

visited = [ [False] * m for _ in range(n)]
        
    
def dfs(x,y):
    global count
    if x>=n or y>=m:
        return 
    # 만약 이미 방문했다면 다음으로 넘어가기 
    if visited[x][y] == True:
        dfs(x,y+1)
    if visited[x][y] == False and floor_list[x][y] =='-':
        visited[x][y]= True
        row_dfs(x,y+1)
        
    if  visited[x][y] == False and floor_list[x][y] =='|':
        visited[x][y]= True
        column_dfs(x+1,y)

def row_dfs(x,y):
    global count
    if y>=m:
        count +=1
        return
    if visited[x][y] ==True:
        count +=1
        return
    if floor_list[x][y] == "-":
        visited[x][y] = True
        row_dfs(x,y+1)
    if floor_list[x][y] == '|':
        count+=1
        return

def column_dfs(x,y):
    global count
    if x>=n:
        count +=1
        return
    if visited[x][y] ==True:
        count +=1
        return
    if floor_list[x][y] == '|':
        visited[x][y]= True
        column_dfs(x+1,y)
    if floor_list[x][y] == '-':
        count+=1
        return
for j in range(n):
    for i in range(m):
        dfs(j,i)
print(count)
            
        