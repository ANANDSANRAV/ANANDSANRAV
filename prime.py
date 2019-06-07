a=int(input())
if(a>1):
      for n in range(2,a):
        if(a%n)==0:
              print("no")
              break
      else:
            print("yes")
else:
      print("no")
      
