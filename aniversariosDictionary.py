aniversarios = {
"Felipe": "12 Julho",
"Henrique": "25 Janeiro",
"Lucas": "7 Setembro",
"Falcirolli": "10 de Abril"}

while True:
    print("Digite um nome: (deixe em branco para sair)")
    name = input()
    #se deixar o nome vazio, sai do loop
    if name == "":
        break

    if name in aniversarios:
        print(aniversarios[name] + " é o aniverário de " + name)
    else:
        print("Eu não tenho o aniversário de " + name + ". Deseja adicionar? (y/n)")
        decisao = input()
        if decisao == "y":
            #print("Digite o nome da pessoa que deseja adicionar")
            #nome = input()
            print("Digite o dia do aniversário de " + name)
            dia = input()
            aniversarios[name]= dia

print("Usando .values() ")
#imprimi tds os values do dictionary (dados do lado direito)
for i in aniversarios.values():
    print (i)
print("----------")
print("Usando .keys()")
#imprimi tds as keys do dictionary (dados do lado esquerdo)
for i in aniversarios.keys():
    print(i)
print("----------")
print("Usando .items()")
#imprimi tds as combinações de dados do dictionary
for i in aniversarios.items():
    print (i)
print("----------")
print("Printando o dictionary")
print(aniversarios)

print("----------")

for i,j in aniversarios.items():
    print("Key: " + i + " | Value: " + j)