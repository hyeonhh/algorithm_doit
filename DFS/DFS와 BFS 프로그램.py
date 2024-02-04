from collections import deque

# 노드의 개수 , 에지의 개수, 탐색을 시작 노드의 번호 V
n,m,v = map(int,(input().split()))


# 인접 리스트  -> 2중 리스트

A = [ [] for _ in range(n+1)] 

# 결과 : 2차원 리스트 -> A = [ [], [], [], [], [] ]

for _ in range(m):
  s,e = map(int,input().split())
  A[s].append(e)
  A[e].append(s)


# 인접 리스트 오름차순으로 정렬하기 , append 시에 오름차순으로 안들어가는 경우가 있으므로
for i in range(n+1):
  A[i].sort()


# 방문 리스트 
visited_list = [False] * (n+1)


# 출력 1 : DFS 수행 시 방문 순서 
def DFS(number):
  print(number,end=" ")
  visited_list[number] = True
  # 인접 리스트에 대해서
  for i in A[number]:
    if not visited_list[i]:
      DFS(i)
     

DFS(v)

# visited_list 초기화
visited_list = [False] * (n+1)

# 출력 2 : BFS 수행시 방문 순서
def BFS(number):
  queue =deque()
  queue.append(number)
  visited_list[number] = True
  while queue:
    now_Node = queue.popleft()
    print(now_Node, end=' ')
    for i in A[now_Node]:
      if not visited_list[i]:
        visited_list[i]= True
        queue.append(i)

print()

BFS(v)