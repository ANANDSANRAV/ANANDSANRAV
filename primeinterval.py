x=input()
y=y.split()
y=list(map(int,y))
y1=a[0]
y2=a[1]
for n in range(y1+1,y2):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n,"",end="")
