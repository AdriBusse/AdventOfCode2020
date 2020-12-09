with open('sample.txt') as file:
  input_ugly = file.read().split('\n')

formattedValues=[]
#[(operation, value, isVisited)]
for singleValue in input_ugly:
  operationValue=singleValue.split(' ')
  formattedValues.append([operationValue[0],int(operationValue[1]),False]) 
print(formattedValues)




def criticalPoint(p):
  if formattedValues[p][2]== True:
    if lastOperation[0]=='jmp':
      print("critical jmp")
      p-= lastOperation[1]
      formattedValues[p][0]='nop'
      p+=1

    if lastOperation[0]=='nop':
      print("critical nop")
      p-=1
      formattedValues[p][0]= 'jmp'
      p+=formattedValues[p][1]
  return p


accumulator=0
pointer=0
n= len(formattedValues)
lastOperation=[]

i=0
while pointer< n-1:
  i+=1
  if i==10:
    break
  lastOperation=formattedValues[pointer]
  print(formattedValues[pointer][0], formattedValues[pointer][1], formattedValues[pointer][2])

  if formattedValues[pointer][0]== 'nop':
    formattedValues[pointer][2]= True
    pointer+=1
    pointer=criticalPoint(pointer)

  elif formattedValues[pointer][0]== 'acc':
    formattedValues[pointer][2]= True
    accumulator+=formattedValues[pointer][1]
    pointer+=1
  elif formattedValues[pointer][0]== 'jmp':
    formattedValues[pointer][2]= True
    pointer+=formattedValues[pointer][1]
    pointer=criticalPoint(pointer)

print(accumulator)