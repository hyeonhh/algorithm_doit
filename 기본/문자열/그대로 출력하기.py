# input_list.append(input_string)

# 리스트 개수는 len(리스트)
# for x in input_list:
#     print(x)

# 줄 구분을 어떻게 하지??
# true인 동안 계속 입력받고 100줄이 넘어가면 끝내는 듯 하다

while True:
    try:
       input_string = input()
       print(input_string)
    except EOFError:
        break 
 
