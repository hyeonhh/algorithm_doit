import sys
sys.setrecursionlimit(10000)


n,m = map(int,input().split())

visited = [False] * (n+1)
link_list = [ [] for _ in range(n+1)]

count = 0


# 간선 정보 입력받기
for _ in range(m):
    u,v = map(int,input().split())
    link_list[u].append(v)
    # 화살표가 없으므로
    link_list[v].append(u)
    
# dfs 함수 구현
    
def dfs(d):
    global visited,count
    # 이미 방문했다면 0 리턴 
    if visited[d]:
        return
    visited[d] = True   
    for i in link_list[d]:
        dfs(i)
    
    
# 연결 리스트의 1번째 요소부터 탐색하기 
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count +=1
print(count)