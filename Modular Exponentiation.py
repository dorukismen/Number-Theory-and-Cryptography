#To understand the code, please look at Read.Me
def modExponentiation(b, e, m):
  c = 1
  i = 0
  while i < e:
   c = (c * b) % m 
   i += 1
  return c
