from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

class Arquivo:
    def __init__(self) -> None:
        pass
        # time.sleep(6)

    def obter_arquivo(self):
        """"""
        button1 = self.driver.find_element_by_id('idSIButton9')
        button1.send_keys(Keys.ENTER)

        time.sleep(30)
        icon = self.driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/messages-header/div[2]/div/team-files/div/team-files-list/div/channel-files-bridge/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/span/span/button')
        mouse = ActionChains(self.driver)
        mouse.context_click(icon).perform()
        time.sleep(3)

        baixar = self.driver.find_element_by_name('Baixar')
        baixar.click()