x=str(input())
y=str(input())
z=0
s=0
if(len(x)==len(y)):
  for i in range(1,len(x)):
    if(x[i]==x[i+1]):
      z=z+1
    if(y[i]==y[i+1]):
      s=s+1
    if(c!=b):
      print("no")
      break
    if(z==s):
     print("yes")
    else:
     print("no")
