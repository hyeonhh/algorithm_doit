# 떡의 개수 n,  요청한 떡의 길이 m
n,m = map(int,input().split())

# 떡의 길이 리스트
rice_cake_list = list(map(int,input().split()))

# 이진 탐색을 위한 시작점 & 끝점
start = 0
end = max(rice_cake_list)

result = 0
# 이진 탐색 반복문 구현
while(start <= end):
  mid = (start + end )//2
  # 잘린 떡의 길이
  total = 0

  for rice_cake in rice_cake_list:
    if mid < rice_cake:
      total += rice_cake-mid

  if total < m:
    end = mid-1
  else:
    result = mid
    start= mid+1

print(result)

