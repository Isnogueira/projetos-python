from selenium import webdriver
import time

class whatsapp_bot():

    def __init__ (self):
        # 1) mensagem
        self.mensagem = "TEST"
        # 2) lista de destinatários
        self.destinatarios = ["Bia Neri", "TEST BOT 2"]
        # 3) linguagem
        options = webdriver.ChromeOptions()
        options.add_argument("lang-pt-br")
        # 4) caminho do chromedriver
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)
    
    def enviar_mensagem (self):
        try:
            self.driver.get("https://web.whatsapp.com/")
            time.sleep(30)

            for destinatario in self.destinatarios:
                # encontrar o destinatario
                campo_destinatario = self.driver.find_element_by_xpath(f"//span[@title='{destinatario}']")
                time.sleep(3)
                # clicar no destinatário
                campo_destinatario.click()
                # encontrar a caixa de texto
                chat_box = self.driver.find_element_by_class_name("_3uMse")
                time.sleep(3)
                # selecionar a caixa de texto
                chat_box.click()
                # escrever mensagem
                chat_box.send_keys(self.mensagem)
                # encontrar o botão enviar
                botao_enviar = self.driver.find_element_by_xpath(f"//span[@data-icon='send']")
                time.sleep(3)
                # clicar no botao de enviar
                botao_enviar.click()
        except: 
            print("Ocorreu um erro inesperado.")

bot_whatsapp = whatsapp_bot()
bot_whatsapp.enviar_mensagem()







