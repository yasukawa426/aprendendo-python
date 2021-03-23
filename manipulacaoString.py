print(
'''alou
td bem?''')
oi = "Hello World!"
print(oi[0])
print(oi[5])
print(oi[8])
print(oi[0:5])
print(oi[6:])


# -------------------------- join() e split() --------------------------
nomes = ['Carlos', 'Michael', "gAy", "noses"]

print (' '.join(nomes))
print (' e '.join(nomes))
print(', '.join(nomes))

frase = "Oi, eu sou eu maa"

print(frase.split())
print(frase.split("u"))
print(frase.split(sep = "u"))#msm coisa

spam = '''Dear Alice, How have you been? I am fine.
There is a container in the fridge 
that is labeled "Milk Experiment". 
Please do not drink it. 
Sincerely, Bob'''

print(spam.split('\n')) #separa a frase td vez q pula uma linha


# -------------------------- formatação --------------------------
print("Hello".rjust(20)) #quantos caracteres vai ter. Se for menor q a string, nada vai acontecer
print("Hello".ljust(20)) 
print("Hello".center(20)) 

#caracteres especiais
#substitui os espaços vazio pelo caractere q vc usar
print("Hello".rjust(20, 'a')) 
print("Hello".ljust(20, "*")) 
print("Hello".center(20, "=")) 


def printPicnic(itemsDict, leftWidth, rightWidth): 
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-')) 
    #para cada par de chave-valor, imprime eles formatados
    for chave, valor in itemsDict.items(): 
        print(chave.ljust(leftWidth, '.') + str(valor).rjust(rightWidth)) 
        

picnicItems = {
'sandwiches': 4,
'apples': 12, 
'cups': 4, 
'cookies': 8000} 
printPicnic(picnicItems, 12, 5) 
printPicnic(picnicItems, 20, 6)



# while True:
#     idade = input("Digite sua idade: ")

#     if idade.isnumeric():
#         break
#     print("Digite um número inteiro*******")

# while True:
#     senha = input("Digite uma nova senha (letras e numeros, apenas): ")

#     if senha.isalnum():
#         break

#     print("Senhas só podem conter letras e números")
# print(idade + "\n" + senha)

