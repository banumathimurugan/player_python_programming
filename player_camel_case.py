s=input("Enter the String:")
def cam(word):
  import re
  return ' '.join(x.capitalizer() or ' ' for x in word.split(' '))
print(cam(s))
