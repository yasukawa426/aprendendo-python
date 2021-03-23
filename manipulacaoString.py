print(
'''alou
td bem?''')
oi = "Hello World!"
print(oi[0])
print(oi[5])
print(oi[8])
print(oi[0:5])
print(oi[6:])

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

