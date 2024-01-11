dnaLength,pwdLenth = map(int, input().split())
dnaList=list(input())

passwordList= list(map(int,input().split()))
currentList=[0]*4

checkSecret=0
result=0

#비번 체크 리스트에서 0인 값이 있으면 checkSecret +1
for i in range(4):
  if passwordList[i]==0:
    checkSecret+=1


# 들어오는 수를 더해주는 로직 d
def addLogic(newValue):
  global checkSecret
  if newValue == "A":      
    currentList[0] +=1
    if currentList[0] == passwordList[0]:
      checkSecret+=1

  elif newValue =="C":
    currentList[1] +=1
    if currentList[1] == passwordList[1]:
      checkSecret +=1

  elif newValue =="G":
    currentList[2] +=1
    if currentList[2] == passwordList[2]:
      checkSecret +=1
  else:
    currentList[3] +=1
    if currentList[3] == passwordList[3]:
      checkSecret +=1




#나가는 수를 빼주는 로직 
def deleteLogic(newValue):
  global checkSecret
  if newValue == "A":
    if currentList[0] == passwordList[0]:
      checkSecret-=1
    currentList[0] -=1
  elif newValue =="C":
    if currentList[1] == passwordList[1]:
      checkSecret-=1
    currentList[1] -=1
  elif newValue =="G":
    if currentList[2]== passwordList[2]:
      checkSecret-=1
    currentList[2] -=1
  else:
    if currentList[3]==passwordList[3]:
      checkSecret-=1
    currentList[3] -=1


#처음 상태 리스트 
for i in range(pwdLenth):
  addLogic(dnaList[i])
if checkSecret==4:
  result+=1


for addIndex in range(pwdLenth,dnaLength):
  deleteIndex = addIndex-pwdLenth
  addLogic(dnaList[addIndex])
  deleteLogic(dnaList[deleteIndex])

  if(checkSecret==4):
    result +=1

print(result)



