import pprint

contador = 0
frase = "Olá, bem vindo "


while contador <= 6:
    print(frase + str(contador))
    contador = contador + 1
    
#contando quantas vezes cada char repete na string

for character in message: 
    count.setdefault(character, 0) 
    count[character] = count[character] + 1 

pprint.pprint(count)