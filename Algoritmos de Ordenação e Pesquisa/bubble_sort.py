def bubble_sort(lista):
    n = len(lista)
    for j in range(0, n):
        for i in range(0, n - j - 1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

lista = [5, 1, 10, 5, 33, 2, 90, -6, 30]

print(bubble_sort(lista))
