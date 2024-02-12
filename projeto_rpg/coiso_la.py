###############
# bibliotecas #
###############

import random as rd

############
# verdades #
############

verdade = True
rolardados = False

##########
# listas #
##########

lista_de_modificadores = ["força", "forca" "destreza", "constituição", "inteligência", "carisma", "for", "des", "const", "int", "car"]

sim = ["s","sim"]
nao = ["n","nao","não"]

forca = ["for","força","forca"]
destreza = ["des","destreza"]
constituição = ["const","constituição"]
inteligencia = ["int","inteligencia"]
sabedoria = ["sab","sabedoria"]
carisma = ["car","carisma"]

fichas = ["darth", "skamos", "5"]

#############
# variaveis #
#############

modificador2 = 0
total = 0
totaltotal = 0

###########
# funções #
###########

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

####################
# inicio do codigo #
####################

print("bom dia Guilherme!")
ficha = input("vai usar qual ficha hoje? ")

if ficha in fichas:
    if ficha == "skamos":
        forc = -1
        des = 2
        const = 2
        inte = 0
        sab = 2
        car = 4
        proef = 3    
    elif ficha == "darth":
        forc = 0
        des = 1
        const = 0
        inte = 1
        sab = 3
        car = 5
        proef = 3    
    elif ficha == "iccarion":
        print("Sinto muito gui, deixe ele descançar")
        print("Ele ja fez muito por nós")
        forc = 5
        des = 1
        const = 3 
        inte = 0
        sab = -1
        car = 3
        proef = 5
        vida = 154

elif ficha not in fichas:
    print("ficha, n encontrada parceiro, deseja inserir modificadores avulsos?")
    inserirmanualmente = input("sim ou não? ")
    if inserirmanualmente in sim:
        print("joia, só não esqueça de salvar os valores no codigo depois.")
        nome_novo = (input("Insira o nome do personagem: "))
        forc = int(input("força: "))
        des = int(input("destreza: "))
        const = int(input("constituição: "))
        inte = int(input("inteligencia: "))
        sab = int(input("sabedoria: "))
        car = int(input("carisma: "))
        proef = int(input("modificador de proeficiencia: "))
        vida = int(input("vida do consagrado: "))
    else:
        print("vai querer só rolar os dados sem nada?")
        vai = input("s ou n? ")
        if vai in sim:
            print("joia")
            

while verdade:
    print("ok, voce vai rolar dados?")
    vai_rolar = input("s ou n?  ")
    if vai_rolar in sim:
        rolardados = True
        print("joia")
        modificador = input("qual atributo vai usar? ")
        if modificador in lista_de_modificadores:
            e_proeficiente = input("é proeficiente? ")
            if e_proeficiente in sim:
                if modificador in forca:
                    modificador2 = forc + proef
                    break
                elif modificador in destreza:
                    modificador2 = des + proef
                    break
                elif modificador in constituição:
                    modificador2 = const + proef
                    break
                elif modificador in inteligencia:
                    modificador2 = inte + proef
                    break
                elif modificador in sabedoria:
                    modificador2 = sab + proef
                    break
                elif modificador in destreza:
                    modificador2 = des + proef
                    break
                elif modificador in carisma:
                    modificador2 = car + proef
                    break
            elif e_proeficiente in nao:
                print("acontece kk")
                if modificador in forca:
                    modificador2 = forc 
                    break
                elif modificador in destreza:
                    modificador2 = des
                    break
                elif modificador in constituição:
                    modificador2 = const 
                    break
                elif modificador in inteligencia:
                    modificador2 = inte
                    break
                elif modificador in sabedoria:
                    modificador2 = sab 
                    break
                elif modificador in destreza:
                    modificador2 = des
                    break
                elif modificador in carisma:
                    modificador2 = car
            else:
                e_proeficiente = input("é proeficiente? ")
                print("responde certo imbecil")
                break
        else:
            print("entendi")

    elif vai_rolar in nao:
        print("joia")
        break
    else:
        print("responde certo imbecil")
    break

if rolardados == True:
    total = lancardados()


print(f"O total deu: {totaltotal}")
