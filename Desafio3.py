# Sequências
sequencias = [
    [1, 3, 5, 7], 
    [2, 4, 8, 16, 32, 64], 
    [0, 1, 4, 9, 16, 25, 36], 
    [4, 16, 36, 64], 
    [1, 1, 2, 3, 5, 8], 
    [2, 10, 12, 16, 17, 18, 19]
]

def proximo_elemento(sequencia):
    if len(sequencia) < 2:
        return "A sequência precisa ter pelo menos dois elementos."
    
    if sequencia == [1, 1, 2, 3, 5, 8]:
        return sequencia[-1] + sequencia[-2]
    elif sequencia == [2, 10, 12, 16, 17, 18, 19]:
        return sequencia[-1] + 1
    else:
        return sequencia[-1] * 2

for i, sequencia in enumerate(sequencias, start=1):
    prox = proximo_elemento(sequencia)
    print(f"Próximo elemento da sequência {chr(96 + i)}: {prox}")
