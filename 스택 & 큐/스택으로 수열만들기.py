lengthOfSu = int(input())
numOfSu=[]
stackOfSu =[]
appendNumber=1
answer =""

resultSu=True

for i in range(lengthOfSu):
  numOfSu.append(int(input()))


for i in range(lengthOfSu):
    if numOfSu[i] >= appendNumber:
        while numOfSu[i]>= appendNumber:
            stackOfSu.append(appendNumber)
            appendNumber += 1
            answer += "+\n"
            
        
        stackOfSu.pop()
        answer += "-\n"
        
    else:
        popOfNum = stackOfSu.pop()
        if popOfNum > numOfSu[i]:
            print("NO")
            resultSu = False
            break
        else:
            answer += "-\n"
            
    
if resultSu:
    print(answer)