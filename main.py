from controllers.login_teams import Login
from controllers.arquivo import Arquivo
from controllers.email import Email
from controllers.config import Config


listEMail = ['']


def start():
    config = Config.get_config()
    l = Login("email", "password")
    a = Arquivo()
    a.obter_arquivo()
    e = Email(listEMail, config['email']['remetente'], config['email']['senha'])
    e.enviar_email()
    
if __name__ == '__main__':
    start()





