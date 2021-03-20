import random

minimo = random.randint(0,100)
maximo = random.randint(minimo, minimo + random.randint(2,1000))
numero = random.randint(minimo + 1, maximo - 1)
print("Estou pensando em um numero entre " + str(minimo) + " e " + str(maximo))
print("Tente adivinhar ")
adivinho = int(input())
contador = 1
while numero != adivinho:
    
    if numero > adivinho:
        print("Mano, adivinhou baixo dms. Tente dnv.")
        adivinho = int(input())
        contador = contador + 1
    elif numero < adivinho:
        print("Mano, adivinhou alto dms. Tente dnv.")
        adivinho = int(input())
        contador = contador + 1
        

print("Booooa, o número era " + str(numero) + ". Adivinhou em " + str(contador) + " tentativas")