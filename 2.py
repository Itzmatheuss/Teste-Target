# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci
#  e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def pertence_fibonacci(numero):
    a, b = 0, 1
    sequencia = [a]

    while b <= numero:
        sequencia.append(b)
        a, b = b, a + b

    print("Sequência de Fibonacci gerada até o número informado:")
    print(sequencia)

    if numero in sequencia:
        return f"\nO número {numero} pertence à sequência de Fibonacci."
    else:
        return f"\nO número {numero} NÃO pertence à sequência de Fibonacci."

# Exemplo de uso:
num = int(input("Digite um número: "))
resultado = pertence_fibonacci(num)
print(resultado)

 