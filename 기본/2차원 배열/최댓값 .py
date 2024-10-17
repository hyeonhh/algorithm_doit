max_list=[]
row_list = []
column_list = []

# 최대값이 있는 행 번호 

# 행 수만큼 행 삽입
for i in range(9):
    row_num = list(map(int,input().split()))
    max_list.append(max(row_num))
    # 현재 행 번호 
    row_list.append(i)
    # 엷 번호
    column_list.append(row_num.index(max(row_num)))
    
print(max(max_list))
max_index = max_list.index(max(max_list))
print(row_list[max_index] +1, end = " ")
print(column_list[max_index] +1 )
