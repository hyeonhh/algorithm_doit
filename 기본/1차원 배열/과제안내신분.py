n_list = []
not_in_n_list = []
for _ in range(28):
    n= int(input())
    n_list.append(n)

for i in range(1, 31):
    if i not in n_list:
        not_in_n_list.append(i)

print(min(not_in_n_list))
print(max(not_in_n_list))



