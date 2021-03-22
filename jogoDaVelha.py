import pprint

def printJogo  (matriz):
    for i in matriz:
        print(i)

def checarGanhou(matriz):
    #x| |
    #x| |
    #x| |
    if jogoVelha[0][0] == jogoVelha[1][0] and jogoVelha[1][0] == jogoVelha[2][0]:
        printJogo(jogoVelha)
        print(str(jogoVelha[0][0]) + " ganhou" )
        return True

    #x| |
    #x| |
    #x| |
    elif jogoVelha[0][0] == jogoVelha[1][0] and jogoVelha[1][0] == jogoVelha[2][0]:
        printJogo(jogoVelha)
        print(str(jogoVelha[0][0]) + " ganhou" )
        return True

    #x| |
    #x| |
    #x| |
    elif jogoVelha[0][0] == jogoVelha[1][0] and jogoVelha[1][0] == jogoVelha[2][0]:
        printJogo(jogoVelha)
        print(str(jogoVelha[0][0]) + " ganhou" )
        return True

    #x| |
    #x| |
    #x| |
    elif jogoVelha[0][0] == jogoVelha[1][0] and jogoVelha[1][0] == jogoVelha[2][0]:
        printJogo(jogoVelha)
        print(str(jogoVelha[0][0]) + " ganhou" )
        return True

    #x| |
    #x| |
    #x| |
    elif jogoVelha[0][0] == jogoVelha[1][0] and jogoVelha[1][0] == jogoVelha[2][0]:
        printJogo(jogoVelha)
        print(str(jogoVelha[0][0]) + " ganhou" )
        return True

    #x| |
    #x| |
    #x| |
    elif jogoVelha[0][0] == jogoVelha[1][0] and jogoVelha[1][0] == jogoVelha[2][0]:
        printJogo(jogoVelha)
        print(str(jogoVelha[0][0]) + " ganhou" )
        return True

    #x| |
    #x| |
    #x| |
    elif jogoVelha[0][0] == jogoVelha[1][0] and jogoVelha[1][0] == jogoVelha[2][0]:
        printJogo(jogoVelha)
        print(str(jogoVelha[0][0]) + " ganhou" )
        return True

    #x| |
    #x| |
    #x| |
    elif jogoVelha[0][0] == jogoVelha[1][0] and jogoVelha[1][0] == jogoVelha[2][0]:
        printJogo(jogoVelha)
        print(str(jogoVelha[0][0]) + " ganhou" )
        return True

    
    return False


jogoVelha = [
[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "],
]

while True:
    printJogo(jogoVelha)
    xLinha = int(input("x, Qual linha vc quer jogar? (apenas numero): "))
    xColuna = int(input("x, Qual coluna vc quer jogar? (apenas numero): ")
)
    jogoVelha[xLinha-1][xColuna-1] = "x"
    ganhou = checarGanhou(jogoVelha)
    if ganhou:
        break

    printJogo(jogoVelha)
    yLinha = int(input("y, Qual linha vc quer jogar? (apenas numero): "))
    yColuna = int(input("y, Qual coluna vc quer jogar? (apenas numero): "))
    
    jogoVelha[yLinha-1][yColuna-1] = "o"
    ganhou = checarGanhou(jogoVelha)
    if ganhou:
        break

    print("--------")
    
    