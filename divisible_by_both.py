x=int(input())
y=int(input())
s=1
while True:
  if (s%x==0) and (s%y==0):
    print(s)
    break
  else:
    s=s+1
