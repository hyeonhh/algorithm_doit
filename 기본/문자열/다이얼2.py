dial_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()

time_result = 0

for i in range(len(word)):
    for dial in dial_list:
        if word[i] in dial:
            time_result += dial_list.index(dial)+3
print(time_result)