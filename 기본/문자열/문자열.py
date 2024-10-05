test_count = int(input())
test_word_list = []
for _ in range(test_count):
    test_word = input()
    test_word_list.append(test_word)
    
for word in test_word_list:
    first = word[0] 
    
    # 문자열의 마지막 요소 접근 시 문자열.strip()[-1]을 해주면 됨
    last = word.strip()[-1]
    print(first,end ='')
    print(last)

