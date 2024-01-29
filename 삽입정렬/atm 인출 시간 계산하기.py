num = int(input())
outTimeList = list(map(int,input().split()))

# outTimeList를 오름차순으로 정렬
  # 정렬값의 인덱스는 1부터 n까지


for i in range(1,num):
  insert_index=i
  insert_value=outTimeList[i]

  for j in range(i-1,-1,-1):
    
    if outTimeList[j] < outTimeList[i]:
      # 이 경우 정렬 필요 없음 
      # 정렬하려는 값이 더 큰 경우
      # -> 인덱스를 줄이다가 
      # 정렬하려는 값보다 배열의 값이 더 작은 경우가 생기면
      # 그 다음에 삽입하면 된다.     
      insert_index = j+1  
      break
    if j==0:
      insert_index=0
      

      # 뒤로 밀기 : 삽입하려는 값-1부터 ~ 삽입할 위치+1 범위이다.  
  for j in range(i,insert_index,-1):
    outTimeList[j] = outTimeList[j-1] 
  outTimeList[insert_index] = insert_value

  # 합배열 생성



S = [0]* num

S[0] = outTimeList[0]


for i in range(1,num):
  S[i] =S[i-1] + outTimeList[i]
  
sum =0
for i in range(1,num):
  sum += S[i]
print(sum)



# outTimeList 시간의 합배열 구하기 


#출력 : 돈을인출하는데 합배열의 최솟값 
  