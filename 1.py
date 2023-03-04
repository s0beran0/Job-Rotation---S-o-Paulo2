# Recebe um número do usuário
numero = int(input("Digite um número inteiro: "))

# Inicializa as variáveis para a sequência de Fibonacci
a, b = 0, 1
fibonacci = [a, b]

# Calcula a sequência de Fibonacci até o número informado ou até que o último número seja maior que o número informado
while b < numero:
    a, b = b, a + b
    fibonacci.append(b)

# Verifica se o número informado pertence à sequência de Fibonacci
if numero in fibonacci:
    print(numero, "pertence à sequência de Fibonacci.")
else:
    print(numero, "não pertence à sequência de Fibonacci.")
