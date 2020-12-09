import re
valid=0
passports= []
with open("input.txt") as file:
  passports= file.read()

passports= passports.split("\n\n")
for passport in passports: 
  passportDic={}
  #m = re.search('((.*):(.*))', passport)
  passport =passport.replace("\n"," ").split(" ")
  #print(passport)
  for entry in passport:
    tmp= entry.split(":")
    passportDic[tmp[0]]=tmp[1]

  requirements= ['eyr','byr','hcl','hgt','ecl','iyr','pid']
  keys = passportDic.keys()
  if 'eyr' in keys and 'byr' in keys and 'hcl' in keys and 'hgt' in keys and 'ecl' in keys and 'iyr' in keys and 'pid' in keys:
    if int(passportDic['byr']) >=1920 and int(passportDic['byr'])<=2002:
      if int(passportDic['iyr'])>= 2010 and int(passportDic['iyr'])<=2020:
        if int(passportDic['eyr'])>=2020 and int(passportDic['eyr'])<=2030:
          if 'cm' in passportDic['hgt'] and int(passportDic['hgt'][:-2])>= 150 and int(passportDic['hgt'][:-2])<=193  or 'in' in passportDic['hgt'] and int(passportDic['hgt'][:-2])>=59 and int(passportDic['hgt'][:-2])<=76:
            if re.search('#([a-f0-9]{6})', passportDic['hcl']):
              if passportDic['ecl']=='amb' or passportDic['ecl']=='blu' or passportDic['ecl']=='brn' or passportDic['ecl']=='gry' or passportDic['ecl']=='grn' or passportDic['ecl']=='hzl' or passportDic['ecl']=='oth':
                if re.search('^\d{9}$', passportDic['pid']):
                  valid+=1
            

    
    
  
print(valid)

  

