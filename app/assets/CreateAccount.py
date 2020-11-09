from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'app/')
import secret, variables

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot      = webdriver.Chrome(executable_path=secret._driverPath)
    
    def createAccount(self):
        bot           = self.bot
        bot.get(secret._create_account_url)
        bot.find_element_by_xpath(variables.disable_popup).click()
        sleep(3)
        # form
        bot.find_element_by_xpath(variables.c_mail).send_keys(secret._mail) #mail
        sleep(1)
        bot.find_element_by_xpath(variables.c_complete_name).send_keys(secret._full_name) # complete
        sleep(1)
        bot.find_element_by_xpath(variables.c_username).send_keys(secret._username) #username
        sleep(1)
        bot.find_element_by_xpath(variables.c_pass).send_keys(secret._pass) #pass
        bot.find_element_by_xpath(variables.c_btn).click() ##doudle # pour ne pas créer tant que je n'ai pas fait la suite 


    #url, mail, pass
    def accessToTheMail(self):
        bot           = self.bot
        bot.execute_script("window.open()")
        bot.switch_to_window(bot.window_handles[1])
        bot.get(secret._mail_url)
        sleep(1)
        bot.find_element_by_xpath(variables.m_mail_input).send_keys(secret._mail + Keys.RETURN)
        sleep(2)
        bot.find_element_by_xpath(variables.m_mail_pass).send_keys(secret._pass + Keys.RETURN)
        sleep(3)
        bot.find_element_by_xpath(variables.m_tab_rs).click()
        bot.find_element_by_xpath("//*[contains(text(), 'Instagram')]")
        sleep(1)





insta = InstagramBot(secret._mail, secret._pass)
#insta.createAccount()
insta.accessToTheMail()

