n, k = map(int,input().split())
a = list(map(int,input().split()))

# 오름차순 정렬 -> 퀵 정렬
def quickSort(s,e,k):
  global a
  if s<e:
    pivot = partitions(s,e)

# swap 함수
def swap(i,j):
  global a
  temp = a[i]
  a[i] = a[j]
  a[j]= temp

# 1. pivot 설정 , 초기 start, end 인덱스 설정 

def partition(s,e):
  global a

# 배열의 길이가 2인 경우는 그냥 swap
  if s +1 == e:
    if a[s] > a[e] :
      swap(s,e)
    return e
  
  m = (s+e) //2
  swap(s,m)
  pivot = A[s]
  i = s+1
  j =e

  while i<=j :
    while pivot < A[j] and j>0:
      j=j-1
    while pivot >A[i] and i <len(A)-1:
      i = i+1
    if i <=j:
      swap(i,j)
      i = i+1
      j = j-1
  a[s] = a[e]
  a[j]= pivot
  return j


