import random, PySimpleGUI as sg

class chute_um_numero():

    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_min = 1
        self.valor_max = 100
        self.tentar_novamente = True
    def iniciar(self):
        # layout
        layout = [
            [sg.Text("Seu chute", size=(10, 0)), sg.Input(size=(3, 0), key="ValorChute")],
            [sg.Button("Chutar!")],
            [sg.Output(size=(39, 10))]
        ]
        # criar uma janela
        self.janela = sg.Window("Chute um número!", layout=layout) 
        self.gerar_num_aleatorio()
        try:
            while True:
                # receber valores
                self.evento, self.valores = self.janela.Read()
                # fazer algo com os valores
                if(self.evento == "Chutar!"):
                    self.valor_do_chute = self.valores["ValorChute"]
                    while (self.tentar_novamente == True):
                        if(int(self.valor_do_chute)) > (self.valor_aleatorio):
                            print("Chute um valor mais baixo!")
                            break
                        elif(int(self.valor_do_chute) < self.valor_aleatorio):
                            print("Chute um valor mais alto!")
                            break
                        elif (int(self.valor_do_chute) == self.valor_aleatorio):
                            self.tentar_novamente == False
                            print("PARABÉNS VOCÊ ACERTOU!")
                            break
                # Fechar janela com o clique
                elif (self.evento == sg.WIN_CLOSED): 
                    break
        except:
            print ("Favor digitar apenas números!")
            self.iniciar()   

    def gerar_num_aleatorio(self):
        self.valor_aleatorio =  random.randint(self.valor_min, self.valor_max)

numero = chute_um_numero()
numero.iniciar()

# update
