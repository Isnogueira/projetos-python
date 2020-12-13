def entra_numero_inteiro(msg):
    
    num_ok = False
    while (not num_ok):
        try:
            num = int(input(msg))
            num_ok = True
        except:
            print(" NÚMERO INVÁLIDO")
    return num

def entra_numero_real(msg):
    
    num_ok = False
    while (not num_ok):
        try:
            num = float(input(msg))
            num_ok = True
        except:
            print(" NÚMERO INVÁLIDO")
    return num

def entra_saldo(msg):

    saldo_ok = False
    while (not saldo_ok):
        saldo = entra_numero_real(msg)
        if (saldo >= 0 ):
            saldo_ok = True
        else:
            print("SALDO INVÁLIDO")
    return saldo

def confirmar():
    
    opcoes = ("s", "S", "n", "N")
    while(True):
        conf = input("Confirma a operação? [s] ou [n] ")
        if(conf in opcoes):
            if((conf in opcoes[0:2])):
                print()
                print("Exclusão feita com sucesso!")
                return True
            else:
                return False
        else:
            print("OPÇAO INVÁLIDA.")

def sacar_depositar():
    
    opcoes = ("d", "D", "s", "S")
    while(True):
        oper = input("Qual a operação desejada? [s]saque ou [d]depósito: ")
        if(oper in opcoes):
            if(oper in opcoes):
                return oper
        else:
            print("OPÇAO INVÁLIDA.")