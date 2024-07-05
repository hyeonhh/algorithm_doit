import sys
input = sys.stdin.readline
INF = int(1e9)


n,m = map(int,input().split())

start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [ [] for i in range(n+1)]

#방문 리스트
visited = [False * n+1]

# 최단 거리 테이블을 무한으로 초기화
distance = [INF] *(n+1)


# 모든 간선 정보 입력받기 
for _ in range(m):
    a,b,c  = map(int,input().split())

    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미 
    graph[a].append((b,c))

# 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_value = INF 
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index=i
    return index

    
def dijkstra(start):
    #시작 노드에 대해 초기화
    distance[start]=0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start=start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])