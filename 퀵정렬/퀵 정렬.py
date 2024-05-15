array = [5,7,9,0,3,1,6,2,4,8]

# 퀵 정렬은 재귀적인 방식으로 동작!

def quick_sort(array):

  # 종료 조건
  if len(array) <=1:
    return array
  
  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return   quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
