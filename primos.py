n_primos = []
contador = 2

def is_prime(n):
  for i in range(2, n):
    if (n%i) == 0:
      return False
  return True

while len(n_primos) < 41:
    resultado = is_prime(contador)
    if resultado == True:
        n_primos.append(contador)
    contador += 1

for i in n_primos:
    print(i)

