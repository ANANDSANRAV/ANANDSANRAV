y=int(input())
sum=0
temp=y
while temp>0:
 d=temp%10
 sum+=d**3
 temp//=10
if(y==sum):
 print("yes")
else:
 print("no")
