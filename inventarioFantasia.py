inventario = {
 "Flecha" : 12,
 "Moeda de Ouro" : 42,
 "Corda" : 1,
 "Tocha" : 4,
 "Adaga" : 1
}

def mostrarInventario(invetario):
    print("Inventario:")
    itensTotais = 0
    #a chave i e o seu valor j
    for chave,valor in inventario.items():
        #print("Chave: " + chave + " Valor: " + str(valor))
        itensTotais = itensTotais + valor
        print(str(valor) + " " + chave.lower()) #.lower() coloca em letra minuscula
        
    print("Total de itens: " + str(itensTotais))
mostrarInventario(inventario)