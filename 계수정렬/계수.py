array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

#정렬할 리스트의 값의 모든 범위를 포함하는 리스트를 선언해준다.
# 모든 값은 0으로 초기화
count =[0] * (max(array+1))

for i in range(len(array)):
  count[array[i]] +=1

  # 인덱스를 확인하면서 해당 인덱스를 값으로 가지는 데이터를 출력
for i in range(len(count)):
  for j in range(count[j]):
    print(i,end=' ')
