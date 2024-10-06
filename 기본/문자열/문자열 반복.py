test_count = int(input())
answer_list = []

for _ in range(test_count):
    r,s = input().split()
    answer = ""
    for word in s:
        answer += word * int(r)
    answer_list.append(answer)

for i in answer_list:
    print(i)