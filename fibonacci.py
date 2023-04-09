# O script verifica se o número escolhido pelo usuário, ou um número fixo colocado diretamente no código, pertence ou não a sequência de Fibonacci.

# usr = int(input('Digite um numero: '))
def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
    if b == n:
        return True
    else:
        return False

def sequencia(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    if n in fib:
        print(f"O numero {n} PERTENCE a sequência de Fibonacci.")
    else:
        print(f"O numero {n} NAO pertence a sequência de Fibonacci.")

# Para colocar a entrada do usuario, comente a linha 24 e tire o comentario das linhas 3 e 23
# sequencia(usr)
sequencia(4)