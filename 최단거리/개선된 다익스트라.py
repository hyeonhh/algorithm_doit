import heapq
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


def dijkstra(start):
    q = []

    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now]  < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1] # i[1] :  노드와 인접한 다른 노드의 거리값 
            if cost < distance[i[0]]:
                #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))



dijkstra(start=start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

