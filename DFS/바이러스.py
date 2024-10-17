n = int(input())
m = int(input())

# 방문 노드 : 노드 개수에 맞춰야함
visited = [False] * (n+1)
count = 0
    
# 인접 리스트  -> 2중 리스트

graph = [ [] for _ in range(n+1)] 

# 결과 : 2차원 리스트 -> A = [ [], [], [], [], [] , [] , []  ]

for _ in range(m):
  s,e = map(int,input().split())
  graph[s].append(e)
  graph[e].append(s)


def dfs(graph, v,visited):
  global count
  visited[v] = True
  for current in graph[v]:
    if not visited[current]:
      count +=1
      dfs(graph,current,visited)
    else:
      continue
  return
      
dfs(graph,1,visited)
print(count)