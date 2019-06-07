t=int(input())
sum=0
temp=t
while temp>0:
 c=temp%10
 sum+=c**3
 temp//=10
if(t==sum):
 print("yes")
else:
 print("no")
