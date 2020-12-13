import PySimpleGUI as sg

class jogo_de_aventura():
    def __init__(self):
        self.pergunta1 = "Você nasceu no norte ou no Sul? (norte/sul) "
        self.pergunta2 = "Você prefere a espada ou escudo? (espada/escudo) "
        self.pergunta3 = "Qual a sua especialidade (linha de frente/tatico)? "
        self.final_historia1 = "Você será um heroi na linha de frente!"
        self.final_historia2 = "Você será um herói protegendo as nossas tropas!"
        self.final_historia3 = "Você irá se sacrificar nessa batalha."
        self.final_historia4 = "Você não é capaz de lutar nessa batalha."

    
    def iniciar(self):
        # layout
        layout = [
            [sg.Button("Iniciar")],
            [sg.Output(size=(50,0))],
            [sg.Input(size=(25,0), key="escolha")],
            [sg.Button("Responder")]
        ]
        # criar janela
        self.janela = sg.Window("Jogo de aventura", layout=layout)
        while True:
                # ler os dados
            self.ler_valores()
                # fazer algo com os dados
            if (self.evento == "Iniciar"):
                print(self.pergunta1)
                self.ler_valores()
                if (self.valores["escolha"] == "norte"):
                    print(self.pergunta2)
                    self.ler_valores()
                    if (self.valores["escolha"] == "espada"):
                        print(self.final_historia1)
                        self.ler_valores()
                    elif (self.valores["escolha"] == "escudo"):
                        print(self.final_historia2)
                        self.ler_valores()
                elif(self.valores["escolha"] == "sul"):
                    print(self.pergunta3)
                    self.ler_valores()
                    if(self.valores["escolha"] == "linha de frente"):
                        print(self.final_historia3)
                        self.ler_valores()
                    elif(self.valores["escolha"] == "tatico"):
                        print(self.final_historia4)
                        self.ler_valores()
                        break
            # Fechar janela com o clique
            elif (self.evento == sg.WIN_CLOSED): 
                break
                    
    def ler_valores(self):
        self.evento, self.valores = self.janela.Read()
            
jogo = jogo_de_aventura()
jogo.iniciar()

# update
# - tratamento de erros
