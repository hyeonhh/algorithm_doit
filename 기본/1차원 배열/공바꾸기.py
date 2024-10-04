n,m = map(int,input().split())
ball_list=[]

for x in range(n):
    ball_list.append(x+1)

for _ in range(m):
    i,j = map(int,input().split())

    ball_list[i-1], ball_list[j-1] = ball_list[j-1],ball_list[i-1]

for ball in ball_list:
    print(ball , end=" ")
