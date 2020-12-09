#Method parsing -> (min,max,letter,password)
def parse(line):
  first = line.split('-',1)[0]
  second = line.split("-")[1].split(" ")[0]
  letter = line.split(' ')[1].split(':')[0]
  pw = line.split(' ')[2]
  return (int(first)-1, int(second)-1, letter, pw)

#Method check if pw is valid
#return 1 if valid otherwhise 0
def check(pwTupel):
  #(args: first, second, letter, pw)
  if pwTupel[3][pwTupel[0]] == pwTupel[2] or pwTupel[3][pwTupel[1]] == pwTupel[2]: 
    if pwTupel[3][pwTupel[0]] == pwTupel[2] and pwTupel[3][pwTupel[1]] == pwTupel[2]:
      return 0
    return 1
  return 0
  


#root level, read file, itterate over lines and call check(parse(liene))
file = open('./input.txt','r')

i=0
for line in file:
  i+= check(parse(line))
  ##print(check(parse("1-10 z: ztzzzgzzzz")))

print(i)

  
  