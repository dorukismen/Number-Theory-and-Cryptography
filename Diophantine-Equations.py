def diophantine(a, b, c):
  assert c % gcd(a, b) == 0
  q, r = divmod(a,b) #divmod operation to compute the quotient and remainder at the same time
  if r == 0:
    return( [0,c/b] )
  else:
    sol = diophantine( b, r, c )
    u = sol[0]
    v = sol[1]
    return( [ v, u - q*v ] )
