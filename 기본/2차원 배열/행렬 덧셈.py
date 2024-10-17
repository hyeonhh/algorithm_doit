n,m = map(int,input().split())

# list에 append로 한 행씩 넣어준다면 []로만 초기화해주면 된다.
a_list = []
b_list =  []

#2차원 배열 초기화
c_list =  [ [0] * m for _ in range(n)]

for i in range(n):
    row_num = list(map(int,input().split()))
    a_list.append(row_num)
    
for i in range(n):
    row_num = list(map(int,input().split()))
    b_list.append(row_num)

for i in range(n):
    for j in range(m):
        c_list[i][j] = a_list[i][j] + b_list[i][j]

for i in range(n):
    for j in range(m):
        print(c_list[i][j], end =" ")
    # 한줄 띄우고 싶으면
    print()