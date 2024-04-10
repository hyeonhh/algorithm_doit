# 순열의 개수 
n = int(input())


def dfs(v):
  visited[v]=1
  next = arr[v]
  if visited[next]==0:
    dfs(next)
  return 
  


for _ in range(n):
  cycle_count =0
  # 순열을 이루는 정수 개수 
  m = int(input())
  # 순열 데이터 
  arr = list(map(int,input().split()))
  
  #방문 리스트
  visited = [0] *( m+1)

  # 순열 리스트 인덱스 1부터 사용하기 위한 조작
  arr.insert(0,0)

  for i in range(1,m+1):
    if visited[i] ==0:
      dfs(i)
      cycle_count +=1
  
  print(cycle_count)

