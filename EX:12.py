n = input("enter the word to check for palindrome:\n")
if( (n.lower() == n.lower()[::-1])):
 print(n,"is  a palindrome.")
else:
  print(n,"is a not palindrome")
