word = input()
n = int(input())

# 문자열에서 인덱스를 이용할 때는 
# word.index(n-1)로 하면 안된다.
# print(word.index(n-1))
print(word[n-1])