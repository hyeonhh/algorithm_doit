word = input().split()
print(len(word))

# split(" ") 가 아니라 그냥 split()을 해주니까 맞았다.
# # 그런데 리스트 순회 도중 리스트 값을 제거하는 것은 위험하다고 한다!
# splited_word = word.split()
# for i in splited_word:
#     if i =='':
#         splited_word.remove(i)
#     else:
#         continue
# print(len(splited_word))