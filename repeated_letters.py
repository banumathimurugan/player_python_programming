def firstRpeatedChar(str):
  a={}
  for ch in str:
    if ch in a:
      return ch;
    else:
      a[ch]=0
  return '\0'
  print(repeated character ("welcome"))
