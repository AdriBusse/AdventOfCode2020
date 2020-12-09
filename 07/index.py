import re
CHECK='shiny gold'
fileInput=[]
with open('input.txt') as f:
  fileInput = f.read().split('\n')

def containsMyBag(liste, farbe): 
  #print("check for "+farbe)
  if len(liste) ==0:
    return False
  for oneColor in liste:
    if farbe == oneColor[1]:
      return True
  return False
#parse input to dict("color":["amount", "color"])
rules= dict()
for line in fileInput:
  color= re.search('^(\w+ \w+)', line)
  canContains= re.findall('((\d) (\w+ \w+))', line)

  rules[color[1]]=[]
  if not canContains:
    continue
  for oneColor in canContains:
    rules[color[1]].append((oneColor[1].strip(),oneColor[2].strip()))

print(rules)


counter =set()
for oneRule in rules.keys():
   
  if containsMyBag(rules[oneRule], CHECK):
    print("find direct in "+oneRule)
    counter.add(oneRule)
    for oneRule1 in rules.keys():

      if containsMyBag(rules[oneRule1],oneRule):
        counter.add(oneRule1)
        print("found in 2 steps in: "+ oneRule1)
        
    


    



print(len(counter))