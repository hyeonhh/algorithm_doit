word = input()

# 단어들을 모두 대문자로 만들어준다.
upper_word = word.upper()
answer ={}
max_value = 0


for w in upper_word:
    if w in answer:
        answer[w] +=1
    else:
        answer[w] =1
        
max_value = max(answer.values())      

#answer.items() : 딕셔너리 의 모든 키- 값 쌍을 튜플로 반환하는 메서드
# answer.items()에서 반환한 (key,value) 튜플을 key와 value 변수에 각각 할당하면서 반복문을 돌린다.
# value가 max_value와 같다면 해당 반복문에서 튜플에 key를 추가해준다.
max_value_list =  [key for key,value in answer.items() if value == max_value]


# 튜플의 길이를 알려면 len(튜플)
if len(max_value_list) >1:
    print("?")
else:
    print(max_value_list[0])


        