s=str(raw_input())
y=list(x)
for x in range (0,len(s)):
  if(x%2==0):
    y[x],y[x+1]=y[x+1],y[x]
print(''.join(y))
