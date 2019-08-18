def gcd(n,m) : # This function finds the greatest common divisor
  if n == 0:
    return m
  return gcd(m % n, n)

def squares(n, m) : # This return for dividing length and width and multiply them, for number of squares.
    return n/gcd(n,m) * m/gcd(n,m) 
