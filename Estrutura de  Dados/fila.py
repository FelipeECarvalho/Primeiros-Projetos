def menu():
    print("[1] - Para enfileirar")
    print("[2] - Para desenfileirar")
    print("[3] - Para ver a fila")
    print("[4] - Para sair")
    opc = int(input("Sua opção: "))
    if opc == 1:
        enfileirar()
    elif opc == 2:
        desenfileirar()
    elif opc == 3:
        mostra_fila()
    elif opc == 4:
        return False
    else:
        print("OPÇÃO INVÁLIDA")
    return True


def vazia():
    if len(fila) == 0:
        return True
    else:
        return False


def enfileirar():
    global fila
    elemento = input("Valor: ")
    fila.append(elemento)


def desenfileirar():
    global fila
    if vazia():
        print("FILA VAZIA!")
    else:
        print(f"--== {fila[0]} DESENFILEIRADO! ==--")
        fila.pop(0)


def mostra_fila():
    global fila
    if vazia():
        print("FILA VAZIA!")
    else:
        for elemento in fila:
            print(elemento, end="<- ")
        print()


fila = []
while True:
   if not menu():
       break
