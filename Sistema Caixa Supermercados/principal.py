from produtos import produto
from time import sleep
import os


def calcula_preco(vezes, codigo):
    preco = vezes * produto[codigo][0]
    return total.append(preco)
    

def compra_vazia():
    if len(itens) == 0 or sum(total) == 0:
        return True
    else:
        return False

# O código é separado, por peso/quantidade e código, ex: 2x7622210194046 = ["2", "7622210194046"]
# Aqui é testado também se o código é codigo de fruta ou de produto, sendo de fruta ele direciona pra função registra_flv(), sendo de produto para registra_produto.
def leitura_codigo():
    codigo = str(input("Código: ")).replace("x", " ").split()
    if len(codigo) == 1:
        if len(codigo[0]) > 4:
            try:
                teste = produto[codigo[0]]
            except (KeyError, IndexError):
                print("[ERRO]: Código inválido")
            else:
                return registra_produto(codigo[0])
        else:
            if codigo[0] == "m":
                return menu()
            else:
                print("[ERRO]: É necessário digitar o peso")
    else:
        try:
            teste = produto[codigo[1]]
        except (KeyError, IndexError):
            print("[ERRO]: Código inválido")
        else:
            return registra_flv(codigo[0], codigo[1])


def registra_produto(codigo):
    vezes = 1
    calcula_preco(vezes, codigo)
    return apresenta_produto(codigo, vezes)


def registra_flv(quant, codigo):
    peso = float(quant)
    calcula_preco(peso, codigo)
    return apresenta_produto(codigo, peso)


def menu():
    print("-----------------------------")
    print("[1] - Para exclusão de item ")
    print("[2] - Para finalizar a venda")
    print("[3] - Para cancelar compra")
    print("[4] - Para fechar o caixa")
    print("[0] - Para voltar           ")
    print("-----------------------------")
    try:
        opcao = int(input("Sua opção: "))
    except ValueError:
        print("[ERRO]: Opção inválida")
    else:
        if opcao == 1: 
            if compra_vazia():
                print("[ERRO]: Não foi possivel excluir - Compra vazia")
            else:
                return exclusao()
        elif opcao == 2:
            if compra_vazia():
                print("[ERRO]: Não foi possivel finalizar - Compra vazia")
            else:
                lista_pagamento = list()
                total_compra = sum(total)
                total_pago = 0
                valor_pago = 0
                valor_a_pagar = total_compra
                return encerra_compra(total_compra, valor_pago, valor_a_pagar, lista_pagamento, total_pago)
        elif opcao == 3:
            if compra_vazia():
                print("[ERRO]: Não foi possivel cancelar - Compra vazia")
            else:
                return cancela_compra()
        elif opcao == 4:
            if not compra_vazia():
                print("[ERRO]: Encerre a compra para fechar o caixa")
            else:
                return fecha_caixa()
        elif opcao == 0:
            return leitura_codigo()
        else:
            print("[ERRO]: Opção inválida")
            return menu()
        
           
def apresenta_produto(codigo, vezes):
    print(f"{cont + 1} - {produto[codigo][1]}  Preço/Kg R${produto[codigo][0]}")
    print(f"    {vezes} x R${produto[codigo][0]} = R${total[cont]:.2f} \n")
    print(f"Total R${sum(total):.2f}")
    guarda_produto(codigo, vezes)



def guarda_produto(cod, quant):
    global cont
    itens.append([produto[cod][1], produto[cod][0], quant, total[cont]])
    cont += 1
    

def exclusao():
    try:
        excluir = int(input("Digite o indice do produto: "))
        excluir -= 1
        if not (itens[excluir] != []):
            print("[ERRO]: índice já excluido")
            return leitura_codigo()
    except (ValueError, IndexError):
        print("[ERRO]: Índice não encontrado")
    else:
        print(f"ITEM  REMOVIDO == {excluir + 1}")
        print(f"    {itens[excluir][2]} x {itens[excluir][1]} = {total[excluir]:.2f}\n")
        total[excluir] = 0
        itens[excluir] = []
        print(f"Total R${sum(total):.2f}")


def encerra_compra(total, pago, pagar, lista_pagamento, total_pago):
    print("-----------------------------")
    print("[1] - Para dinheiro          ")
    print("[4] - Para crédito a vista   ")
    print("[5] - Para crédito parcelado ")
    print("[7] - Para débito            ")
    print("[0] - Para cancelar          ")
    print("-----------------------------")
    print()
    total_pago += pago
    pago = 0
    print(f"VALOR PAGO: R${total_pago:.2f}   TOTAL A PAGAR: R${pagar:.2f}    TOTAL: R${total:.2f}")
    print()
    try:
        pagamento = int(input("Forma de pagamento: "))
    except ValueError:
        print("[ERRO]: Opção inválida")
        return encerra_compra(total, pago, pagar, lista_pagamento, total_pago)
    else:
        if pagamento == 1:
            dinheiro(total, pago, pagar, lista_pagamento, total_pago)
        elif pagamento == 4:
            credito(total, pago, pagar, lista_pagamento, total_pago)
        elif pagamento == 5:
            credito_parcelado(total, pago, pagar, lista_pagamento, total_pago)
        elif pagamento == 7:
            debito(total, pago, pagar, lista_pagamento, total_pago)
        elif pagamento == 0:
            return leitura_codigo()
        else:
            print("[ERRO]: Opção inválida")
            return encerra_compra(total, pago, pagar, lista_pagamento, total_pago)

# Na opção de pagamento em dinheiro, é testado se o valor pago é maior ou menor que o valor a pagar, sendo menor ele tira o valor pago do valor a pagar e retorna a função encerra pagamento, sendo o valor maior ele chama a função imprime_nota e calcula o troco
def dinheiro(total, pago, pagar, lista_pagamento, total_pago):
    try:
        pago = float(input("Digite a quantidade: R$"))
        pago = round(pago, 2)
    except ValueError:
        print("[ERRO]: Digite apenas valores numéricos")
        return dinheiro(total, pago, pagar, lista_pagamento, total_pago)
    else:
        # Todas as formas de pgamento são guardadas na lista_pagamento
        lista_pagamento.append(["DINHEIRO", pago])
        if pago < pagar:
            pagar -= pago
            pagar = round(pagar, 2)
            return encerra_compra(total, pago, pagar, lista_pagamento, total_pago)
        else:
            total_pago += pago
            troco = total_pago - total
            print(f"Troco: R${troco:.2f}")
            input("Pressione Entra caso o troco for realizado:")
            imprime_nota(total, troco, lista_pagamento)


# Nas opções de pagamento em cartão, todas fazem quase a mesma coisa, verifica se o valor pago é menor que o valor a pagar, sendo menor ele retira o valor pago do valor a pagar, e retorna a função encerra compra, sendo o valor pago maior que o valor a pagar, ele acusa um erro, sendo o valor pago igual ao valor a pagar, ele encerra a compra, e imprime a nota.
def credito(total, pago, pagar, lista_pagamento, total_pago):
    try:
        pago = float(input("Digite a quantidade: R$"))
        pago = round(pago, 2)
    except ValueError:
        print("[ERRO]: Digite valores numéricos")
        return credito(total, pago, pagar, lista_pagamento, total_pago)
    else:
        if pago < pagar:
            lista_pagamento.append(["CREDITO A VISTA", pago])
            pagar -= pago
            pagar = round(pagar, 2)
            return encerra_compra(total, pago, pagar, lista_pagamento, total_pago)
        elif pago > pagar:
            print("[ERRO]: Forma de pagamento não aceita troco")
            pago = 0
            return encerra_compra(total, pago, pagar, lista_pagamento, total_pago)
        else:
            lista_pagamento.append(["CREDITO A VISTA", pago])
            troco = 0
            total_pago += pago
            imprime_nota(total, troco, lista_pagamento)


def credito_parcelado(total, pago, pagar, lista_pagamento, total_pago):
    try:
        pago = float(input("Digite a quantidade: R$"))
        pago = round(pago, 2)
        vezes = int(input("Parcelas: "))
    except ValueError:
        print("[ERRO]: Digite valores numéricos")
        return credito_parcelado(total, pago, pagar, lista_pagamento, total_pago)
    else:
        if pago < pagar:
            pagar -= pago
            pagar = round(pagar, 2)
            lista_pagamento.append(["CREDITO PARCELADO", vezes, pago])
            return encerra_compra(total, pago, pagar, lista_pagamento, total_pago)
        elif pago > pagar:
            print("[ERRO]: Forma de pagamento não aceita troco")
            pago = 0
            return encerra_compra(total, pago, pagar, lista_pagamento, total_pago)
        else:
            lista_pagamento.append(["CREDITO PARCELADO", vezes, pago])
            troco = 0
            total_pago += pago
            imprime_nota(total, troco, lista_pagamento)


def debito(total, pago, pagar, lista_pagamento, total_pago):
    try:
        pago = float(input("Digite a quantidade: R$"))
        pago = round(pago, 2)
    except ValueError:
        print("[ERRO]: Digite valores numéricos")
        return debito(total, pago, pagar, lista_pagamento, total_pago)
    else:
        if pago < pagar:
            lista_pagamento.append(["DEBITO", pago])
            pagar -= pago
            pagar = round(pagar, 2)
            return encerra_compra(total, pago, pagar, lista_pagamento, total_pago)
        elif pago > pagar:
            print("[ERRO]: Forma de pagamento não aceita troco")
            pago = 0
            return encerra_compra(total, pago, pagar, lista_pagamento, total_pago)
        else:
            lista_pagamento.append(["DEBITO", pago])
            troco = 0
            total_pago += pago
            imprime_nota(total, troco, lista_pagamento)

#Função que formata a lista e retira os itens excluidos da compra
def formata_lista(lista):
    lista_formatada = []
    for elemento in lista:
        if not (elemento == []):
            lista_formatada.append(elemento)
    return lista_formatada

# Mostra os itens da compra, já formatados, e mostra as formas de pagamento.
def imprime_nota(total, troco, lista_pagamento):
    print("Imprimindo Cupom Fiscal...")
    print()
    sleep(2)
    soma = 0
    nova_lista = formata_lista(itens)
    for i, elemento in enumerate(nova_lista):
        print(f"{i + 1} - {nova_lista[i][0]}  Preço/Kg R${nova_lista[i][1]}")
        print(f"   {nova_lista[i][2]} x R${nova_lista[i][1]:.2f} = R${nova_lista[i][3]:.2f} \n")
    print("TOTAL:", end="                                   ")
    print(f"{total:<1.2f}")
    for elemento in lista_pagamento:
        if len(elemento) == 3:
            print(f"     {elemento[0]} {elemento[1]:<4}", end="")
            print(f"{elemento[2]:>20.2f}")
            soma += elemento[2]
            transacoes_finalizadas.append([elemento[0], elemento[2]])
        else:
            print(f"     {elemento[0]:<16}", end="")
            print(f"{elemento[1]:>26.2f}")
            soma += elemento[1]
            transacoes_finalizadas.append([elemento[0], elemento[1]])
    print("SOMA:", end="                                    ")
    print(f"{soma:<1.2f}")
    print("TROCO:", end="                                   ")
    print(f"{troco:<1.2f}")
    input("Pressione Entra para encerrar")
    nova_compra()
    
#Depois de impressa a nota fiscal, é encerrada a compra, sendo resetados o contador, e as listas que guardam produtos e o valor da compra
def nova_compra():
    global itens
    global total
    global cont
    itens = list()
    total = list()
    cont = 0
    os.system('cls')

# É cancelada a compra, também resetando os valores das variáveis
def cancela_compra():
    global itens
    global total
    global cont
    itens = list()
    total = list()
    cont = 0
    print("---- COMPRA CANCELADA ----")
    sleep(1)
    os.system('cls')

# Para fechar o caixa é primeiro verificado se há venda sendo realizada, não havendo, ele mostra todas as transações realizadas, e pede para o usuário elimina-las, depois de eliminadas é encerrado o caixa.
def fecha_caixa():
    global aberto
    tot = 0
    for elemento in transacoes_finalizadas:
        tot += elemento[1]
    print(f"TOTAL DE VENDAS R${tot:.2f}")
    print()
    while len(transacoes_finalizadas) != 0:
        print("ELIMINE AS TRANSAÇÕES FINALIZADAS:")
        for i, elemento in enumerate(transacoes_finalizadas):
            print(f"{i:<1}", end="|    ")
            print(f"{elemento[0]:<17}", end="|")
            print(f"{elemento[1]:>5.2f}")
        try:
            aux = int(input(""))
            tot -= transacoes_finalizadas[aux][1]
            tot = round(tot, 2)
            transacoes_finalizadas.pop(aux)
        except ValueError:
            print("[ERRO]: Digite valores válidos")
            return fecha_caixa()
        except IndexError:
            print(f" Indice <= {len(transacoes_finalizadas)}")
    print(f"TRANSAÇÕES ELIMINADAS TOTAL: R${tot}")
    print("CAIXA FECHADO COM SUCESSO!")
    aberto = False
    

itens = list()
total = list()
transacoes_finalizadas = list()
cont = 0
aberto = True
while aberto:
    leitura_codigo() 

    
