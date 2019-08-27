def ChineseRemainderTheorem(n1, r1, n2, r2):
  (x, y) = ExtendedEuclid(n1, n2) #We have access to Extended Euclid funciton
  n = x*n1*r2 + y*n2*r1
  return n % (n1 * n2)
