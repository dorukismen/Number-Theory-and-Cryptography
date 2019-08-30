def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)

def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b

def PowMod(a, n, mod):
    if n == 0:
        return 1 % mod
    elif n == 1:
        return a % mod
    else:
        b = PowMod(a, n // 2, mod)
        b = b * b % mod
        if n % 2 == 0:
          return b
        else:
          return b * a % mod

def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]


def Encrypt(message, modulo, exponent):
  # Substitute this implementation with your code from question 1 of the "RSA Quiz".
  return PowMod(ConvertToInt(message), exponent, modulo)

def Decrypt(ciphertext, p, q, exponent): #Our main function to decrypt the message which is known ciphertext, keys (p,q), exponent
  #Fix this code
  number = (p-1)*(q-1)
  d = InvertModulo(exponent, number)
  return ConvertToStr(PowMod(ciphertext, d, p * q )) #Int gelecek bunlar degil
  
a = 3
b = 7
c = InvertModulo(a, b)
print(c)

p = 1000000007
q = 1000000009
exponent = 23917
modulo = p * q
ciphertext = Encrypt("attack", modulo, exponent)
message = Decrypt(ciphertext, p, q, exponent)
print(message)
