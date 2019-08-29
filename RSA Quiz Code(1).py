import sys, threading


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

def ConvertToInt(message_str):  # Converts message to integers 
  res = 0
  for i in range(len(message_str)):
    res = res * 256 + ord(message_str[i])
  return res
  
def PowMod(a, n, mod): # Converts message(int), exponent, public key to ciphertext 
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

def Encrypt(message, modulo, exponent):
  # Fix this implementation
  return PowMod(ConvertToInt(message), exponent, modulo)
