
def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[1+ j] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

array = [4, 1, 2, 7, 54, -1, 3, 4, 2, 1, 0, 10]
print(insertion_sort(array))