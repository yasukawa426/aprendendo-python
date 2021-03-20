aniversarios = {
"Felipe": "12 Julho",
"Henrique": "25 Janeiro",
"Lucas": "7 Setembro"}

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
