inventario = {
 "moeda de ouro" : 42,
 "corda" : 1,
}
lootDragao = ['moeda de ouro','adaga','moeda de ouro','moeda de ouro','ruby']

def mostrarInventario(invetario):
    print("Inventario:")
    itensTotais = 0
    #a chave i e o seu valor j
    for chave,valor in inventario.items():
        #print("Chave: " + chave + " Valor: " + str(valor))
        itensTotais = itensTotais + valor
        print(str(valor) + " " + chave) #.lower() coloca em letra minuscula

    print("Total de itens: " + str(itensTotais))

def addParaIventario (inventario, itens):
    



mostrarInventario(inventario)