# 데이터 개수
num = int(input())

# 입력 리스트 

inputList = list(map(int,input().split()))

# 찾아야 할 숫자 개수

findNum  = int(input())

# 찾아야 할 수 리스트 

findList = list(map(int,input().split()))

# 입력 리스트 정렬
inputList.sort()

# 시작, 끝 인덱스

for i in range(findNum):
  find = False
  start = 0
  end = len(inputList)-1
  target = findList[i]
  # 이진 탐색 시작 
  while start <= end:
    midi = int((start+end)/2)
    midiValue = inputList[midi]

    if midiValue > target:
      end = midi-1
    elif midiValue < target:
      start = midi+1
    else:
      find = True
      break
  if find:
    print(1)  
  else:
    print(0)

