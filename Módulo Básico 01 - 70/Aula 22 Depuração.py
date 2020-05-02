#==========================================
#=========  Curso de Phyton   =============
#==========================================

"""
O que é Depuração?
Técnica empregada para entender o funcionamento de um código.
Por vezes empregada afim de descobrir erros de código, em outras, com a finalidade de entender o funcionamento.

"""

acao = int(input("Digite '1' para sim e digite '2' par não: "))

if acao == 1:
    print('Você disse que sim!')
else:
    if acao == 2:
        print('Você disse que não!')
    else:
        print("O numero digitado não é '1' nem '2'.")
