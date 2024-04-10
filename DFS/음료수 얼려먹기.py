# 입력 행과 열의 개수
n, m = map(int,input().split())
graph = []

# 그래프 입력 받기
for i in range(n):
  graph.append(list(map(int,input())))


# dfs 실행
def dfs(x,y):
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False
  if graph[x][y]==0:
    graph[x][y]=1
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True
  return False

icecream = 0

for i in range(n):
  for j in range(m):
    if dfs(i,j)==True:
      icecream+=1

print(icecream)


