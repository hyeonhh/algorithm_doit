remain_list = []
for _ in range(10):
    n = int(input())
    remain_list.append(n%42)

print(len(set(remain_list)))