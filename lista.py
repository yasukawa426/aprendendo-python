def listaToString(lista):
    frase = ""
    for i in range(len(lista)):
        if i == len(lista) - 2:
            frase = frase + lista[i] +" and " + lista[i+1]
            break

        frase = frase + lista[i] + ", " 
    return frase

lista = ["oi","bataa","carne", "jaaaa", "iglo", "carlos"]
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['.', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.']]
#para 6 linhas
for i in range(6):
    #vou imprimir cada coluna
    for j in range(9):
        print(grid[j][i], end="") #printa a lista ao contrario sem quebrar a linha
    print("") #quebra a linha quando terminar de printar a linha


print(listaToString(lista))
