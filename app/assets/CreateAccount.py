from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
sys.path.insert(1, 'app/')
import secret, variables
from selenium.webdriver.support.ui import Select
from time import sleep


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot      = webdriver.Chrome(executable_path=secret._driverPath)
    
    def createAccount(self):
        bot           = self.bot
        bot.get(secret._create_account_url)
        bot.find_element_by_xpath(variables.disable_popup).click()
        sleep(1)
        # form
        bot.find_element_by_xpath(variables.c_mail).send_keys(secret._mail) #mail
        sleep(1)
        bot.find_element_by_xpath(variables.c_complete_name).send_keys(secret._full_name) # complete
        sleep(1)
        bot.find_element_by_xpath(variables.c_username).send_keys(secret._username) #username
        sleep(1)
        bot.find_element_by_xpath(variables.c_pass).send_keys(secret._pass +Keys.RETURN) #pass
        
        # exeptions #
        # select_year = Select(bot.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select"))
        # select_year.select_by_index(21)
        # sleep(2)
       

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
        # bot.find_element_by_xpath("//*[@id='gs_lc50']/input[1]").send_keys("instagram" + Keys.RETURN)
        # bot.find_element_by_xpath('//div[contains(text(), "{0}") and @class="inner"]'.format(text)).click()





insta = InstagramBot(secret._mail, secret._pass)
insta.createAccount()
sleep(3)
#insta.accessToTheMail()

