def menu():
    print("[1] - Para empilhar")
    print("[2] - Para desempilhar")
    print("[3] - Para ver a pilha")
    print("[4] - Para sair")
    opc = int(input("Sua opção: "))
    if opc == 1:
        empilhar()
    elif opc == 2:
        desempilhar()
    elif opc == 3:
        mostra_pilha()
    elif opc == 4:
        return False
    else:
        print("OPÇÃO INVÁLIDA")
    return True


def vazia():
    if len(pilha) == 0:
        return True
    else:
        return False


def empilhar():
    global pilha, topo
    elemento = input("Valor: ")
    topo += 1
    pilha.append(elemento)


def desempilhar():
    global pilha, topo
    if vazia():
        print("PILHA VAZIA!")
    else:
        topo -= 1
        print(f"--== {pilha[topo]} DESEMPILHADO! ==--")
        pilha.pop(topo)


def mostra_pilha():
    global pilha, topo
    if vazia():
        print("PILHA VAZIA!")
    else:
        for i in range(topo-1, -1, -1):
            print(f"{i}º  {pilha[i]}")



pilha = []
topo = 0
while True:
   if not menu():
       break
