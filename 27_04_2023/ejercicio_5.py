#F(n) = F(n-1)+F(n-2)

numero = int(input("Ingresa un numero para saber la suma de la secuencia de Fibonacci hasta ese numero: "))

total = 0
# Esta funcion es recursiva, es decir, se llama a si misma, para calcular el valor de la secuencia de fibonacci
def fibonacci(numero):
    if numero > 1:
        return fibonacci(numero-1)+ fibonacci(numero-2)
    elif numero == 1:
        return 1
    elif numero == 0:
        return 0
    
# Se hace un ciclo para sumar los valores de la secuencia de fibonacci hasta el numero ingresado
for i in range(numero):
    total += fibonacci(i)

# Se imprime el total
print(total)
