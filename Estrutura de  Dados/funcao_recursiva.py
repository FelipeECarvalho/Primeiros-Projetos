def soma(array):
    if len(array) == 0:
        return 0
    else:
        return  array[0] + soma(array[1:])

def conta(array):
    if len(array) == 0:
        return 0
    else:
        return 1 + conta(array[1:])

def maior(array):
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    val_max = maior(array[1:])
    return array[0] if array[0] > val_max else val_max


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


lista = [0, 5, 3, 7, 4, 10, 100, 2, 5, 6, 8, 9, 44, -3]
n = lista[10]

print(f"A soma entre os termos da lista é igual: {soma(lista)}")
print(f"A quantidade de termos da lista é igual: {conta(lista)}")
print(f"O maior elemento do array é igual: {maior(lista)}")
print(f"O indice {n} na sequência fibonacci é igual a: {fibonacci(n)}")
