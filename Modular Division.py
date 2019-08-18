def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a
  return max(a, b)
  
def extended_gcd (a, b):
  # assert a >= b and b >= 0 and a + b > 0
  if b == 0:
    d, x, y = a, 1, 0
  else:
    (d, p, q) = extended_gcd (b, a % b)
    x = q
    y = p - q * (a // b)
  assert a % d == 0 and b % d == 0
  assert d == a * x + b * y
  return (d, x, y)
  
def divide(a, b, n):
  assert n > 1 and a > 0 and gcd(a, n) == 1
  d, t, s = extended_gcd (a, n)
  if t < 0:
    t = t + n
    return t * b % n
  else:
    return t * b % n
  
  assert x >= 0 and n - 1 >= x
  # return the number x s.t. x = b / a (mod n) and 0 <= x <= n-1.
