# 입력 1부터 n까지의 바구니에 m번 공을 넣는다.
n,m = map(int,input().split())
pocket_list = [0] * n


for _ in range(m):
    i,j,k = map(int,input().split())
    # 이미 공이 들어와있다면 빼준다.
    for x in range(i-1,j):
        pocket_list[x] = k

for pocket in pocket_list:
    print(pocket,end=" ")


