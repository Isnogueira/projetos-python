from biblioteca import *
import os, sys

class Conta():
    
    def __init__(self, num, nome, saldo):
        self.num = num
        self.nome = nome
        self.saldo = saldo
        
    def set_num(self, num):
        self.num = num
    
    def get_num(self):
        return self.num
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_nome(self):
        return self.nome
    
    def set_saldo(self, valor):
        self.saldo = valor
    
    def get_saldo(self):
        return self.saldo 
    
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self, valor):
        self.saldo -= valor

def mostrar_menu():
    
    OPCOES = (0, 1, 2, 3, 4, 5)
    opcao_ok = False
    while (not opcao_ok):
        print("--- Sistema Bancário ---")
        print()
        print("1 - Inclusão")
        print("2 - Alteração")
        print("3 - Exclusão")
        print("4 - Movimentar")
        print("5 - Listar")
        print("0 - Sair")
        print()
        opcao = entra_numero_inteiro("Entre com a opção: ")
        if (opcao not in OPCOES):
            print("OPÇÃO INVÁLIDA!")
        else:
            opcao_ok = True
    return opcao

def pesquisa_contas(contas, num_conta):
    
    achou = False
    for conta in contas:
        if(conta.num == num_conta):
            achou = True
        return achou

def pesquisa_contas_index(contas, num_conta):
    
    index = -1
    for i in range(len(contas)):
        if(contas[i].get_num() == num_conta):
            index = i
    return index

def incluir(contas):
    
    print()
    num_conta = entra_numero_inteiro("Entre com o número da conta: ")
    achou = pesquisa_contas(contas, num_conta)
    if(achou):
        print()
        print("Erro: conta já existe")
        print()
    else:
        nome = input("Entre com o nome: ")
        saldo = entra_saldo("Entre com o saldo: R$ ")
        contas.append(Conta(num_conta, nome, saldo))
        print()
        print("Dados cadastrados com sucesso!")
        print()

def alterar(contas):
    
    if (not contas):
        print("Não existem contas a serem alteradas.")
        print()
    num_conta = entra_numero_inteiro("Entre com o número da conta que você quer alterar: ")
    index = pesquisa_contas_index(contas, num_conta)
    if (index == -1):
        print("Erro: conta não existe")
        print()
        return
    novo_nome = input("Entre com o nome atual: ")
    novo_saldo = entra_saldo("Entre com o saldo atual: R$ ")
    contas[index].set_nome(novo_nome)
    contas[index].set_saldo(novo_saldo)
    print()
    print("Alteração feita com sucesso!")

def excluir(contas):
    
    if (not contas):
        print()
        print("Nenhuma conta cadastrada.")
        print()
    num_conta = entra_numero_inteiro("Entre com o número da conta que você deseja excluir: ")
    index = pesquisa_contas_index(contas, num_conta)   
    if(index == -1):
        print("Erro: conta não existe")      
        print() 
        return
    if (confirmar()):
        del contas[index]
    print()

def movimentar(contas):
    
    if (not contas):
        print()
        print("Não existem contas a serem movimentadas.")
        print()
    num_conta = entra_numero_inteiro("Entre com o número da conta que você quer movimentar: ")
    index = pesquisa_contas_index(contas, num_conta)
    if (index == -1):
        print()
        print("Erro: conta não existe")
        print()
        return   
    op = sacar_depositar()
    if (op == "d") or (op == "D"):
        print()
        valor = entra_numero_real("Entre com o valor do depósito: R$ ")
        if (valor <= -1):
            print()
            print("ERRO: Não é possível depositar esse valor.")
            print()
        else:
            contas[index].depositar(valor)
            print()
            print("Depósito feito com sucesso!")
            print()
    elif (op == "s") or (op == "S"):
        print()
        valor = entra_numero_real("Entre com o valor do saque: R$ ")
        if (valor <= -1):
            print()
            print("ERRO: Não é possível sacar esse valor")
            print()
        else:
            contas[index].sacar(valor)
            print()
            print("Saque feito com sucesso!")
            print()
    else:
        print()
        print("Resposta inválida!")
        
def listar(contas):
    
    if (not contas):
        print()
        print("Nenhuma conta cadastrada.")
        print()
    for conta in contas:
        print()
        print("=" * 20)
        print(f"Conta: {conta.num}\nNome: {conta.nome}\nSaldo: R$ {conta.saldo}")
        print("="* 20)

def executar_operacao(contas, opcao):
    
    if (opcao == 1):
        incluir(contas)
        print()
    elif (opcao == 2):
        alterar(contas)
        print()
    elif (opcao == 3):
        excluir(contas)
        print()
    elif (opcao == 4):
        movimentar(contas)
    else:
        listar(contas)
        print()

def ler_arquivo(contas):
    
    # abrir arquivo
    with open(NOME_ARQUIVO, "r") as arq:
        # ler cada linha do arquivo
        for reg in arq.readlines():
            # Quebrar cada registro em campos
            campos = reg.split(";")
            # setar cada campo
            num = int(campos[0])
            nome = campos[1]
            saldo = float(campos[2])
            # criar conta
            contas.append(Conta(num, nome, saldo))
        
def gravar_arquivo(contas):

    #abrir o arquivo
    with open(NOME_ARQUIVO, "w") as arq:
        #percorrer o arquivo de contas e gravar contas no arquivo
        for conta in contas:
            # pegar o objeto conta criar o registro para fazer gravação em texto
            # transformar um objeto numa string
            reg = f"{str(conta.get_num())}; {str(conta.get_nome())}; {str(conta.get_saldo())}"
            arq.write(f"{reg} \n")

NOME_ARQUIVO = "Contas.txt"
# junta o nome do diretório atual com o NOME_ARQUIVO
NOME_ARQUIVO = os.path.join(sys.path[0], NOME_ARQUIVO)

def main():
    contas = []
    ler_arquivo(contas)
    FIM = 0
    opcao = mostrar_menu()
    while (opcao != FIM):
        executar_operacao(contas, opcao)
        opcao = mostrar_menu()
    gravar_arquivo(contas)
    print()
    print("FIM DO PROGRAMA!")
        
if __name__ == "__main__":
    main()