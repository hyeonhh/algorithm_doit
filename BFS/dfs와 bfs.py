from collections import deque
n,m,v = map(int,input().split())

graph = [ [] for _ in range(n+1)]
visited = [False] * (n+1)
visited_bfs = [False] * (n+1)

stack = []
stack_bfs = []

for _ in range(m):
    n1, n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    graph[n1].sort()
    graph[n2].sort()
    

    
def dfs(start):
    stack.append(start) # 1
    visited[start] = True # 1, 
    for j in graph[start]:
        if not visited[j]:
            dfs(j)

deq= deque()

def bfs(start):
    stack_bfs.append(start) # 조사한 노드 순서 1 -> 
    visited_bfs[start] = True
    for i in graph[start]:
        if not visited_bfs[i]:
            deq.appendleft(i)
            visited_bfs[i] = True
    while deq:
        bfs(deq.pop())

            
    
    
        
    

dfs(v)
bfs(v)

for d in stack:
    print(d , end = " ")
print()
for b in stack_bfs:
    print(b , end = " ")