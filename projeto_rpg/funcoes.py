###############
# bibliotecas #
###############

import random as rd


def lancardados():
    dados = {
        "d4": 4,
        "d6": 6,
        "d8": 8,
        "d10": 10,
        "d12": 12,
        "d20": 20
    }
    total = 0
    nmr_de_dados = int(input("Digite o número de dados que você quer lançar: "))
    tipo = input("Digite o tipo de dado que deseja lançar (d4, d6, d8, d10, d12, d20): ")
    
    if tipo in dados:
        lados = dados[tipo]
        while nmr_de_dados >= 1:
            d = rd.randint(1, lados)
            total = total + d
            nmr_de_dados = nmr_de_dados - 1
            print(f"total {total}")
    else:
        print("Tipo de dado inválido.")

    return total