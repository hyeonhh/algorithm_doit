# 자릿수 입력
import math

N = int(input())
number=0

# 소수 구하기

def primenumber(x):
  for i in range (2, int(math.sqrt(x) + 1 ) ):
    if x % i ==0:
      return False
  return True





# DFS 구현

def DFS(number):
  # 자릿수가 N과 같아지면 print
  if len(str(number)) == N:
    print(number)
    
  else:
    for i in range(1,10):
      # 뒤에 붙인 새로운 수가 홀수이면서 소수일 때
      # DFS(수*10 + 뒤에 붙는 수) 실행

      if i % 2==0:
        continue
      if primenumber(number*10 + i):
        DFS(number*10 + i)


#DFS 실행(숫자 2,3,5,7로 탐색 시작)
DFS(2)
DFS(3)
DFS(5)
DFS(7)

