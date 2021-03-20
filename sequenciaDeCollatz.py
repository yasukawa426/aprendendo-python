def collatz(numero):
    #se for par
    if numero % 2 == 0:
        numero = numero // 2
        print(numero)
        return numero
    else:
        numero = 3 * numero + 1
        print(numero)
        return numero

print ("Digite um numero inteiro maior q 1")
digite = None
while digite == None:    
    try:
        digite = int(input())
    except ValueError:
        print("Número não inteiro digitado. Digite novamente")

while digite != 1:
    digite = collatz(digite)