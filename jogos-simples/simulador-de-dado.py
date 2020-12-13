import random
import PySimpleGUI as sg

class simulador_de_dado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # layout
        self.layout = [
            [sg.Button("Jogar o dado")],
            [sg.Text("Resultado:")],[sg.Output(size=(5,0))]
            ]
        
    def iniciar(self):
        # criar uma janela
        self.janela = sg.Window("Simulador de Dado", layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer algo com esses valores
        try:
            while True:    
                if (self.eventos == "Jogar o dado"):
                    self.gerar_valor_do_dado()
                    self.eventos, self.valores = self.janela.Read()
                # Fechar janela com o clique
                elif (self.eventos == sg.WIN_CLOSED):
                    break
        except:
            print("Ocorreu um erro ao receber sua resposta.")

                
    def gerar_valor_do_dado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
    
simulador = simulador_de_dado()

simulador.iniciar()

