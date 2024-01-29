
from collections import deque
numOfCard = int(input())
cardQueue = deque()

for i in range(1,numOfCard+1):
  cardQueue.append(i)


while len(cardQueue)>1:
  cardQueue.popleft()
  cardQueue.append(cardQueue.popleft())

print(cardQueue[0])