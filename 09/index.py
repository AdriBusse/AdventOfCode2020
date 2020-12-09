with open('input.txt') as file:
  numberlistgly = file.readlines()


numberList=[]
for number in numberlistgly:
  numberList.append(int(number.replace('\n', '')))
def part_one():
  counter=25
  def findSum(c):
    minI= c-25
    #max exclusive
    maxI=c
    canContainList= numberList[minI:maxI]

    for number in canContainList:

      for secNumber in canContainList:
        if number==secNumber:
          continue
        if number+ secNumber == numberList[counter]:
          return True
    return False
    
  while counter <= len(numberList)-1:
    a=0
    if not findSum(counter):
      print(numberList[counter])
    
    #print(numberList[counter])
    counter+=1

toFind=530627549
#toFind=127
lowIndex=0
highIndex=0

for number in numberList:
  partSum=[number]
  #highIndex=lowIndex
  tmpList = numberList[lowIndex+1:-1]
  for newNumber in tmpList:
    partSum.append(newNumber)
    if sum(partSum)> toFind:
      break
    if sum(partSum) == toFind:
      print(partSum)
      print(sum(partSum))
      print(partSum[0])
      print(partSum[-1])
      print(min(partSum)+max(partSum))
      break

  lowIndex+=1

