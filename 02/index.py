#Method parsing -> (min,max,letter,password)
def parse(line):
  min = line.split('-',1)[0]
  max = line.split("-")[1].split(" ")[0]
  letter = line.split(' ')[1].split(':')[0]
  pw = line.split(' ')[2]
  return (int(min), int(max), letter, pw)

#Method check if pw is valid
#return 1 if valid otherwhise 0
def check(pwTupel):
  #(args: min, max, letter, pw)
  countLetter=0
  for i in range(len(pwTupel[3])):
    if pwTupel[3][i]== pwTupel[2]:
      countLetter+=1
  if countLetter >= pwTupel[0] and countLetter<= pwTupel[1]:
    return 1
  return 0


#root level, read file, itterate over lines and call check(parse(liene))
file = open('./input.txt','r')

i=0
for line in file:
  i+= check(parse(line))

print(i)
  
  