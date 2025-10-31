def armstrong (num):
  if num == 0 :
    return "not a suitable number"

  n = num # it is a copy of num which is used later bcz by the end of loop the num will bocame 0 
  total = 0 
  power = len(str(num))

  while num > 0 :
    digit = num % 10 
    total += digit **power
    num = num //10 

  if total == n : # here it is used n 
    return " it is a armstrong number"
  
  else :
    return "not a armstrong number"
     

print(armstrong(153))