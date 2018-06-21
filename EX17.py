n = int(input("Enter a number to check for armstrong number: ")) 
sum=0 
p=n 
while p > 0: 
  l=(p%10) 
  sum+=l** 3 
  p//= 10 
if(n==sum): 
  print(n,"Is an Armstrong number") 
else: 
  print(n,"Is not an Armstrong number")
