#==========================================
#=========  Curso de Phyton   =============
#==========================================

"""
Atribuição condicional é uma estrutura para simplificar o código,
onde este valor a ser atribuído será aquele que satisfazer a condição.

"""
num1 = int(input("Digite um número: "))

if num1 %2 == 0:
    s = "par"

else:
    s = "ímpar"

print("O número {} é {}".format(num1, s))


"""
s = "par" if num1 %2 == 0 else "ímpar"
print("O número {} é {}".format(num1, s))
"""

