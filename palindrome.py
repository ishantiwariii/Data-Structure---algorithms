num = input("enter the input ! ")
rev = num[::-1]

if num.lower() == rev.lower():
  print("The given input is palindrome")

else :
  print("The given input is not palindrome")