INF = int(1e9)

n = int(input()) # 노드의 개수 
m = int(input()) # 간선의 개수  

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신 -> 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] =0


# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
# k : 거쳐가는 노드, a : 출발 노드, b : 도착 노드 
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print("INFINITY")
        else:
            print(graph[a][b], end=" ")
    print()