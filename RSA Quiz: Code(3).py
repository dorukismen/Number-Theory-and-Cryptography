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

def ConvertToInt(message_str):
  res = 0
  for i in range(len(message_str)):
    res = res * 256 + ord(message_str[i])
  return res

def Encrypt(message, modulo, exponent):
  # Substitute this implementation with your code from question 1 of the "RSA Quiz".
  return PowMod(ConvertToInt(message), exponent, modulo)

def DecipherSimple(ciphertext, modulo, exponent, potential_messages): #Main function to attack the ciphertext
  # Fix this implementation
  for i in range(len(potential_messages)):
    if ciphertext == Encrypt(potential_messages[i], modulo, exponent):
      return potential_messages[i]
  return "don't know"

modulo = 101
exponent = 12
ciphertext = Encrypt("attack", modulo, exponent)
print(ciphertext)
print(DecipherSimple(ciphertext, modulo, exponent, ["attack", "don't attack", "wait"]))
