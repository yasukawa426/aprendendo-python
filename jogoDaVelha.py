import pprint

def printJogo  (matriz):
    for i in matriz:
        print(i)

def deuVelha (matriz):
    #percorre a matriz td checando se existe algum espaço vazio, se sim, retorna true
    for i in matriz:
        resposta = " " in i
        if resposta == True:
            return False
    return True

def checarGanhou(matriz, jogador):
    #x| |
    #x| |
    #x| |
    if matriz[0][0] == matriz[1][0] and matriz[1][0] == matriz[2][0] and matriz[0][0] == jogador:
        printJogo(matriz)
        print(str(matriz[0][0]) + " ganhou" )
        return True

    #x| |
    # |x|
    # | |x
    elif matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2] and matriz[0][0] == jogador:
        printJogo(matriz)
        print(str(matriz[0][0]) + " ganhou" )
        return True

    #x|x|x
    # | |
    # | |
    elif matriz[0][0] == matriz[0][1] and matriz[0][1] == matriz[0][2] and matriz[0][0] == jogador:
        printJogo(matriz)
        print(str(matriz[0][0]) + " ganhou" )
        return True

    # |x| 
    # |x| 
    # |x| 
    elif matriz[0][1] == matriz[1][1] and matriz[1][1] == matriz[2][1] and matriz[0][1] == jogador:
        printJogo(matriz)
        print(str(matriz[0][1]) + " ganhou" )
        return True

    # | |x
    # | |x
    # | |x
    elif matriz[0][2] == matriz[1][2] and matriz[1][2] == matriz[2][2] and matriz[0][2] == jogador:
        printJogo(matriz)
        print(str(matriz[0][2]) + " ganhou" )
        return True

    # | |
    #x|x|x
    # | |
    elif matriz[1][0] == matriz[1][1] and matriz[1][1] == matriz[1][2] and matriz[1][0] == jogador:
        printJogo(matriz)
        print(str(matriz[0][1]) + " ganhou" )
        return True

    # | |x
    # |x|
    #x| |
    elif matriz[0][2] == matriz[1][1] and matriz[2][0] == matriz[1][1] and matriz[2][0] == jogador:
        printJogo(matriz)
        print(str(matriz[0][2]) + " ganhou" )
        return True

    # | |
    # | |
    #x|x|x
    elif matriz[2][0] == matriz[2][1] and matriz[2][1] == matriz[2][2] and matriz[2][0] == jogador:
        printJogo(matriz)
        print(str(matriz[2][0]) + " ganhou" )
        return True
    
    else:
        #se deu velhar, return velha
        if deuVelha(matriz):
            return "velha"

    
    return False


jogoVelha = [
[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "],
]
ganhou = False
while True:
    printJogo(jogoVelha)
    xLinha = int(input("x, Qual linha vc quer jogar? (apenas numero): "))
    xColuna = int(input("x, Qual coluna vc quer jogar? (apenas numero): ")
)
    jogoVelha[xLinha-1][xColuna-1] = "x"
    ganhou = checarGanhou(jogoVelha,"x")

    printJogo(jogoVelha)
    if ganhou == True:
        break
    elif ganhou == "velha":
        print("Deu velha!")
        break
    yLinha = int(input("y, Qual linha vc quer jogar? (apenas numero): "))
    yColuna = int(input("y, Qual coluna vc quer jogar? (apenas numero): "))
    
    jogoVelha[yLinha-1][yColuna-1] = "o"
    printJogo(jogoVelha)
    ganhou = checarGanhou(jogoVelha,"o")
    if ganhou:
        break
    elif ganhou == "velha":
        print("Deu velha!")
        break

    print("-----------------------------")
    
    