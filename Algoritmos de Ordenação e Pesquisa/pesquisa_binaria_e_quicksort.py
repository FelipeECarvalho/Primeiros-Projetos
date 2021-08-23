def pesquisa_binaria(lista, item):
    inicio = 0
    fim = len(lista) -1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if item == lista[meio]:
            return meio
        else:
            if item > lista[meio]:
                inicio = meio + 1
            else:
                fim = meio - 1


def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        maiores = []
        menores = []
        for i in range(1, len(lista)):
            if lista[i] > pivo:
                maiores.append(lista[i])
            else:
                menores.append(lista[i])
        return quicksort(menores) + [pivo] + quicksort(maiores)



lista = [5, 4, 9, 5, 10, 22, 1, -7, -3, 28, 15]
lista = quicksort(lista)
print(lista)
procura = 10
print(f"O elemento {procura} foi encontrado na posição {pesquisa_binaria(lista, procura)}")