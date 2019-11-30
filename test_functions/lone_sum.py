def lone_sum(a, b, c):
  if (a==b) and (a!=c):
    return c
  elif (a==c) and (b!=c):
    return b
  elif (b==c) and (a!=c):
    return a
  elif (a==c) and (b==c):
    return 0
  else:
    return a+b+c
    
