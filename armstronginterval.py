x1,x2=input("").split()
x1=int(x1)
x2=int(x2)
for i in range(x1,x2):
     s=0
     t=a
     while(a!=0):
          r=a%10;
          s=s+r*r*r;
          a//=10;
     if(t==s):
        print(t,end=" ")
