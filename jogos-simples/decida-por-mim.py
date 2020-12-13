import random, PySimpleGUI as sg

class decida_por_mim():

    def __init__(self):
        self.exemplo_respostas = [
            "Com certeza, você deve fazer isso.",
            "Não sei, você que sabe.",
            "Não faça isso!",
            "Acho que tá na hora certa!"
        ]
        self.pergunta = [sg.Input()]
        self.respostas_escolhidas = []
    
    def iniciar(self):
        # layout
        layout = [
            [sg.Text("Faça sua pergunta")],
            self.pergunta,
            [sg.Button("Decida por mim!")],
            [sg.Output(size=(40, 0))]
        ]
        # criar a janela
        self.janela = sg.Window("Decida por mim!", layout=layout)
        try:   
            while True:
                # ler os valores
                self.eventos, self.valores = self.janela.Read()
                # fazer algo com os valores
                if (self.eventos == "Decida por mim!"):
                    resposta = random.choice(self.exemplo_respostas)
                    self.respostas_escolhidas.append(resposta)
                    for i in range(len(self.respostas_escolhidas)):
                        print(self.respostas_escolhidas[i])
                    if (self.valores != self.pergunta):
                        self.respostas_escolhidas.remove(resposta)
                        print()
                # Fechar janela com o clique
                elif (self.eventos == sg.WIN_CLOSED): 
                    break
        except:
            print("ocorreu um erro inesperado")            
decida = decida_por_mim()   
decida.iniciar()


# UPDATE
# - Apagar as respostas conforme as perguntas são feitas:
#      * Remover duplicata de resposta
#      * Quando a pergunta não mudar, a resposta não mudar    
