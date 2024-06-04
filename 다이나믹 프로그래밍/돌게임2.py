import sys

input = sys.stdin.readline

N = int(input())

# dp = [0] * 

# dp[0] = 0 
# dp[1] = 0 # 0이면 상근 1이면 창영


# # for i in range(2,N):
# #   if dp[i-1] == 0:
# #     dp[i] = 1
# #   else :
# #     dp[i] = 0

if N % 2 ==0:
  print("SK")
else:
  print("CY")

# if dp[N-1] == 0:
#   print("SK")
# else:
#   print("CY")
