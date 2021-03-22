import pprint

def printJogo  (matriz):
    for i in matriz:
        print(i)

jogoVelha = [
[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "],
]
naoTerminou = True
while naoTerminou:
    printJogo(jogoVelha)
    xLinha = int(input("x, Qual linha vc quer jogar? (apenas numero): "))
    xColuna = int(input("x, Qual coluna vc quer jogar? (apenas numero): ")
)
    jogoVelha[xLinha-1][xColuna-1] = "x"

    pprint.pprint(jogoVelha)
    yLinha = int(input("y, Qual linha vc quer jogar? (apenas numero): "))
    yColuna = int(input("y, Qual coluna vc quer jogar? (apenas numero): "))

    jogoVelha[yLinha-1][yColuna-1] = "o"
   
    #x| |
    #x| |
    #x| |
    if jogoVelha[0][0] == jogoVelha[1][0] and jogoVelha[1][0] == jogoVelha[2][0]:
        
        print(str(jogoVelha[0][0]) + " ganhou" )
        naoTerminou= False