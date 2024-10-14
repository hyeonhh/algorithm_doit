word_num = int(input())
count = 0

def check_groud_word():
    checked_word=[]
    word= input()
    # 0번째 요소는 checked_word 리스트에 저장
    for w in word:
        if len(checked_word)==0:
            checked_word.append(w)
            continue
        if checked_word[-1] == w:
            continue
        else:
            if w in checked_word:
                print("그룹 단어 아님")
                return 0
            else:
                checked_word.append(w)
                print("다음")                
                continue
                
for i in range(word_num):
    if check_groud_word() != 0:
        count +=1 
print(count)
            