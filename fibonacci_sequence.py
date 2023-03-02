def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)

for x in range(int(input("elige el numero de veces que quieres que se repita: "))):
    print(fib(x))