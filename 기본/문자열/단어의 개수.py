word = input()
# print(len(word))

# split(" ") 가 아니라 그냥 split()을 해주니까 맞았다.
splited_word = word.split()
for i in splited_word:
    if i =='':
        splited_word.remove(i)
    else:
        continue
print(len(splited_word))