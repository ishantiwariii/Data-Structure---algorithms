num = int(input('enter a number ! '))
li = []
li2 = []
for i in range (1 , num+1):
  if num % i == 0 :
    li.append(i)
  
  else :
    li2.append(i)
  
print(f'here is the factors {li}')
print(f'here is the non factors {li2}')