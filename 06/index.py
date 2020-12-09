rawInput=[]
with open('input.txt')as file:
  rawInput= file.read().split('\n\n')

result=0
for group in rawInput:
  group= group.split('\n')
  setsOfGrpMbs=[]
  isSimilar=set()
  
  for member in group:
    setofMember= set()

    for letter in member:

      setofMember.add(letter)
    setsOfGrpMbs.append(setofMember)
  isSimilar=setsOfGrpMbs[0]
  for oneSet in setsOfGrpMbs:
    isSimilar=isSimilar.intersection(oneSet)
  result+=len(isSimilar)
print(result)




