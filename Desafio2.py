def fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def verifica_pertence(numero, fib_sequence):
    if numero in fib_sequence:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

numero_informado = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

sequencia_fibonacci = fibonacci(numero_informado)

resultado = verifica_pertence(numero_informado, sequencia_fibonacci)

print(resultado)
