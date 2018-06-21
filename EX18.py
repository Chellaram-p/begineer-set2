n=int(input("Enter the 1st no: "))
m=int(input("Enter the 2nd no: "))
for num in range(n,m+1):
   sum=0
   l=num
   while l>0:
       k=l%10
       sum+=k**3
       l//=10
   if (num==sum):
       print(num)
