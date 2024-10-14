chess_list = [1,1,2,2,2,8]

input_chess= list(map(int,input().split()))
result_chess = [0] * 6

for i in range(6):
    result_chess[i] = chess_list[i] - input_chess[i]

for chess in result_chess:
    print(chess, end=" ")
