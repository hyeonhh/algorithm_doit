n,k = map(int,input().split())
result =0



# while n>1:
#   if n%k==0:
#     count +=1
#     n = n //k
#   else:
#     n -= 1
#     count +=1

# while n>=k:
#   while n %k != 0:
#     n -=1
#     count +=1
#   n //=k
#   count +=1
 
# while n>1:
#   n-=1
#   count+=1

while True:
  target = (n//k) * k # k로 나누어떨어지는 수를 구해줌
  result += (n-target) # 1을 빼야할 횟수를 result에 더해줌 
  n = target # target을 n 값에 넣어줌 
  if n<k:
    break
  result +=1 # n이 k보다 크다면 계속 나누는 연산을 수행할 것이다 result에 1씩 더해준다.
  n //= k # k로 n을 나누어준다. 

result += (n-1) 

print(result)