#==========================================
#=========  Curso de Phyton   =============
#==========================================

num1 = int(input("Digite um número: "))

if num1 > 10:
    print("O número digitado é maior que 10")

    if num1 < 15:
        print("O número digitado é maior que 10 mas menor que 15 ")

    else:
        if num1 < 50:
            print("O número digitado é menor que 50")

        else:
            print("O número digitado é maior que 50!")


else:
    if num1 > 5:
        print("O número digitado é menor que 10 mas maior que 5")

        if num1 == 7:
            print("O número digitado é igual a 7 ")

    else:
        print("O valor é menor que 5")
