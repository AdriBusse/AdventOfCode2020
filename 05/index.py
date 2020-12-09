FileInput=[]
usedSeats=[]
with open('input.txt') as f:
  FileInput=f.read().split('\n')

def binparser(bin: list):
  summe=0
  faktor = 1
  for b in bin[::-1]:
    if b == '1':
      summe+=faktor
    faktor=faktor * 2
  return summe

def seatId(row, collumn):
  return row *8 + collumn

for seat in FileInput:
  seatRow= list(seat[0:7].replace('F','0').replace('B','1'))
  seatColumn= list(seat[7:10].replace('R','1').replace('L','0'))
  usedSeats.append(seatId(binparser(seatRow), binparser(seatColumn)))


print(max(usedSeats))
print(len(usedSeats))
#add frontLine
for i in range(0,8):
  print(i)
  usedSeats.append(0*8+i)
#add BackLine
for i in range(0,8):
  usedSeats.append(127*8+i)

#print(128*8)
#print(len(usedSeats))
for i in range(len(usedSeats)+1):
  if i not in usedSeats:
    print(i, ' is not included')