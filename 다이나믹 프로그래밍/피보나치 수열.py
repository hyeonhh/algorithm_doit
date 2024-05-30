def fibo(x):
  if x==1 or x ==2:
    return 1
  return fibo(x-1) + fibo(x-2)

print(fibo(4))


# 재귀함수를 만들 때해는 무한 반복하지 않도록 종료조건을 적어줘야한다! 
# x 가 1 또는 2일 때가 종료 조건이다.

