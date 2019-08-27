def FastModularExponentiation_(b, k, m):
   for i in range(k):
      b = (b * b) % m 
  # your code here
   return b
   
def FastModularExponentiation(b, e, m):
    n = ""
    answer = 1
    while e != 0:
        n = n + str(e % 2)
        e = int(e // 2)
    for i in range(len(n)):
        if n[i] == '1':
            answer*=FastModularExponentiation_(b,i,m)
        answer = answer % m
    return answer
# With this code all of the Modular Exponentiation problems could been solved.

print(FastModularExponentiation(7,128,11)) #For test method
