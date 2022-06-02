# from click import pass_obj
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

class Login:
    def __init__(self, email: str, password: str) -> None:
        """Construtor responsável 
        """
        self.email = email
        self.passoword = password
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--lang=pt-BR')
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument('--log-level=3')
        self.driver = webdriver.Chrome('/home/renatxinha/Robo-send-Workmap/chromedriver', options=chrome_options)
        ('Entrando no site...')
        self.driver.get('link da pasta no teams')
        time.sleep(6)

    def fazer_login(self) -> None:
        """Função responsavél por fazer o login na plataforma do Teams.
        """
        print('Fazendo login...')
        usuario = self.driver.find_element_by_id('i0116')
        usuario.send_keys(self.email)
        usuario.send_keys(Keys.ENTER)
        time.sleep(3)
        password = self.driver.find_element_by_id('i0118')
        password.send_keys(self.passoword)
        password.send_keys(Keys.ENTER)
    
    def continuar_login(self) -> None:
        """Essa função supera a página de 'Continuar Login'
        """
        button1 = self.driver.find_element_by_id('idSIButton9')
        button1.send_keys(Keys.ENTER)
        time.sleep(40)
    
    def baixar_aquivo(self) -> None:
        """Baixa o arquivo pptx da plataforma do Teams.
        """
        icon = self.driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/messages-header/div[2]/div/team-files/div/team-files-list/div/channel-files-bridge/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/span/span/button')
        mouse = ActionChains(self.driver)
        mouse.context_click(icon).perform()
        time.sleep(5)

        baixar = self.driver.find_element_by_name('Baixar')
        baixar.click()
        print('Baixando arquivo...')
        time.sleep(60)
        



        