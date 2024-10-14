# croatia_alpabet = {"c=" :" č", "c-" : "ć" , "dz=" :"dž", "d-":"đ", "lj" : "lj","nj": "nj","s=" : "š","z=" :"ž" }

# input_word = input()
# modity_input_word=""
# modity_input_word = input_word
# crotia_list=[]
# count = 0

# # 크로아티아 단어가 몇개있는지 검사하기 
# for key in croatia_alpabet.keys():
#     while key in modity_input_word:
#         find_index = modity_input_word.find(key)
#         if find_index==-1:
#             break
#         count +=1 
#         # print(input_word[find_index:find_index+len(x)])
#         modity_input_word = modity_input_word.replace(key,"*",1)
#         # nljj의 경우 lj를 발견하면 n과 j가 남는다.
#         crotia_list.append(key)
# # print(len(crotia_list))
# # print(len(list(modity_input_word)))   


# if modity_input_word.find("*") >-1:
#     result = [char for char in modity_input_word if char != '*']
#     # modity_input_word = (modity_input_word.split("*"))
#     count += len(result)
# print(count)
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(word)
print(len(word))