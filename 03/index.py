def makeStep(pos,x,y):
  #print(pos)
  neuX= pos[0]+x
  neuY= pos[1]+y
  neuX= neuX % len(row[0])
  return (neuX, neuY)

def runDown(x,y):
  hit=0
  #(x, y) koordinates
  position= (0,0)
  while position[1]<=len(row)-1:
    #print(row[position[1]][position[0]])
    if row[position[1]][position[0]]=='#':
      hit+=1

    position= makeStep(position,x,y)
  return hit

row= []
with open('input.txt') as file:
  row = file.read().splitlines()

total= 1
print(runDown(1,1))
print(runDown(3,1))
print(runDown(5,1))
print(runDown(7,1))
print(runDown(1,2))
total = runDown(1,1)* runDown(3,1)* runDown(5,1)* runDown(7,1)* runDown(1,2)

print(total)

