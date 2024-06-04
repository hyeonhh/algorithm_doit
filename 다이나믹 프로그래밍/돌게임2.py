import sys

input = sys.stdin.readline

N = int(input())

dp = [-1] * 1001 

dp[1] = 'CY' # 0이면 상근 1이면 창영이가 이김 
dp[2] = 'SK'
dp[3] = 'CY'


for i in range(4,N+1):
  if dp[i-1] == 'CY'or dp[i-3]=='CY':
    dp[i] = 'SK'
  else :
    dp[i] = 'CY'

print(dp[N])