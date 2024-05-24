array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
  min_index = i
  for j in range(i+1,len(array)):
    if array[min_index] > array[j]:
      min_index = j
    # 현재 가장 작은 인덱스를 가장 앞쪽 원소와 바꿔준다.
    array[i] , array[min_index] = array[min_index] , array[i]

print(array)