test = int(input())


def sum_func(x):
  if x==1:
    return 1
  elif x==2:
    return 2
  elif x==3:
    return 4
  else:
    return sum_func(x-1) + sum_func(x-2) + sum_func(x-3)
  
                              


for _ in range(0,test):
  n = int(input())
  print(sum_func(n))
