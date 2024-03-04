from collections import deque

# 상하좌우 탐색을 위한 리스트 선언
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# n.m 입력 
n,m = map(int,input().split())

# n개의 줄에 미로 내용을 m개의 정수로 표현

# A 리스트 초기화
A = [ [0] * m for _ in range(n)]

# 방문 리스트 초기화
visited = [[False] *(m) for _ in range(n) ]
    

# A 리스트 채우기 
for i in range(n):
  numbers = list(input())
  for j in range(m):
    A[i][j] = int(numbers[j])
 
 
 # BFS 구현
def BFS(i,j):
  queue= deque()
  queue.append((i,j))
  visited[i][j] = True

  while queue:
    now = queue.popleft()
    for k in range(4):
      x = now[0] + dx[k]
      y = now[1] + dy[k]
      if x>=0 and y>=0 and x < n and y <m: # 좌표 상으로 유효한 범위인지를 확인한다. -1 과가 같은 좌표나 현재 공간보다 큰 좌표는 제외
        if A[x][y] != 0 and not visited[x][y]:
          visited[x][y] = True
          A[x][y] = A[now[0]][now[1]]+1
          queue.append((x,y))






# 출력 : 지나야하는 칸 수의 최솟값
          
BFS(0,0)
print(A[n-1][m-1])