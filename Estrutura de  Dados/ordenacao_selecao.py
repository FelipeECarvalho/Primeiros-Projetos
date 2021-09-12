def ordena_sel(lista):
    for i in range(len(lista) - 1):
        menor_indice = i
        for k, elemento in enumerate(lista[i+1:], start=i + 1):
            if elemento < lista[menor_indice]:
                menor_indice = k
        if menor_indice != i:
            lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
    return lista

lista = [9, 3, 2, 7, 4, 3, 1, 9, 0, -5, 22, 65]
print(ordena_sel(lista))