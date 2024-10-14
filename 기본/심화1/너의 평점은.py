num_score_total_count = 0
total = 0
result = 0
num_score_dic = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0,
}



def calculate_score():
    global num_score_total_count,total
    class_name, class_num_score, class_score= input().split()
    if class_score != 'P':
        num_score_total_count += float(class_num_score)
        total += float(class_num_score)* num_score_dic[class_score]
        

for _ in range(20):
    calculate_score()
    
result = total / num_score_total_count

print("{:.6f}".format(result))