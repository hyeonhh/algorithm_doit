def binary_search(array, target, start, end):
  while start <= end:
    if start > end:
      return None
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      return binary_search(array,target,start , mid-1)
    else:
      return binary_search(array, target, mid+1, end)
  return None

n =  int(input())
n_list = list(map(int,input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int,input().split()))

for target in m_list:
  result = binary_search(n_list,target,0,n)
  if result != None:
    print("yes", end =' ')
  else:
    print("no", end=' ')