import sys

input = sys.stdin.readline

N = int(input())

dp = [-1] * 1001 

dp[1] = 1 # 0이면 상근 1이면 창영이가 이김 
dp[2] = 0
dp[3] = 1


for i in range(4,N+1):
  if dp[i-1] or dp[i-3]:
    dp[i] = 0
  else :
    dp[i] = 1

if dp[N] == 0:
  print("SK")
else:
  print("CY")