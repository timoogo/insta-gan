from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
sys.path.insert(1, 'app/')
from selenium.webdriver.support.ui import Select
from time import sleep




# Create account : c_@variable
c_mail ="//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input"
c_complete_name = "//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/div/label/input"
c_username ="//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[5]/div/label/input"
c_pass = "//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[6]/div/label/input"
c_btn = "//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[7]/div/button"
disable_popup ='/html/body/div[2]/div/div/div/div[2]/button[1]'
#dropdown myd

#mois
c_select_m ="//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select"
c_mounth_o = "//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[@value='11']"

#day 
c_select_d = "//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select"
c_day_o = "//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[9]"

#year
# c_select_y ="//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select"
# c_year_o = "//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[21]" # 2000


# Mail : m_@variable
m_mail_input = '//*[@id="identifierId"]'
m_mail_pass = '//*[@id="password"]/div[1]/div/div[1]/input'
m_tab_rs ="//*[@id=':27']"