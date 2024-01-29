n,m = map(int,input().split())

# visited list 
visitied = [False] * (n+1)

# 인접 리스트 
A = [ [] for _ in range(n+1)] 

# 결과 : 2차원 리스트 -> A = [ [], [], [], [], [] 가 n개 만들어진다. ]
                                                          
for _ in range(m):
  s,e = map(int,input().split())
  A[s].append(e)
  A[e].append(s)
  
  

# DFS 재귀 함수 
def DFS(v):
  visitied[v] = True
  for i in A[v]:
    if not visitied[i]:
      DFS(i)
      
# 연결 요소의 개수       
count = 0
for i in range(1,n+1):
  if not visitied[i]:
    count +=1
    DFS(i)


print(count)
