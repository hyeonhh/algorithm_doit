import heapq
import sys

num = int(sys.stdin.readline())
heap=[]


for i in range(num):
  info = int(sys.stdin.readline())
  if info != 0:
    # x값을 배열에 추가 
    # 절댓값이 작은 것이 우선순위가 된다. 
    heapq.heappush(heap,(abs(info),info))
  else:
    #배열이 비어있는 경우
    if len(heap)==0 :  
      print("0")
    # 배열이 비어있지 않은 경우
    else:
      # 절댓값이 가장 작은 값을 출력, 음수 우선
      temp = heapq.heappop(heap)
      print(temp[1])


