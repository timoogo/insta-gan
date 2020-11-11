from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys, os 
import secret
from time import sleep, ctime

from selenium.webdriver.support.ui import Select
pathtoaccess = "/Users/timogo/Sites/insta-gan/app/assets/BestHashtagsOfTheDate/"
temp_txt = "tagList.txt"
filetmp = pathtoaccess + temp_txt
now = str("Dernière MAJ : %s" % ctime()) + "\n"
class External:
    def __init__(self):
        self.bot      = webdriver.Chrome(executable_path=secret._driverPath)
    
    def fileToWriteOn(self, file, c):

        bot = self.bot
        print(os.getcwd())
        os.chdir(pathtoaccess)
        print(os.getcwd())
        self.createTmp(file)
       
        
        
    def createTmp(self, file):
        bot = self.bot
        with open(file, 'w+') as fp: 
            pass
    
    def getHashTagsTrend(self, file):
        bot = self.bot
        bot.get('https://www.all-hashtag.com/top-hashtags.php')
        sleep(3)
        #if durationClassname = "tab1" :    
        texts = [el.text for el in bot.find_elements_by_class_name("hashtag")]
        textstr = '\n'.join(texts)
        self.fileToWriteOn(file, textstr)
        h = open(file, "w+")
        h.write(now)
        h.write(textstr)
        h.close()
        
        
        
    def Quit(self):
        bot = self.bot
        print("fin de process")
        bot.quit()
        

            
            
ext = External()
ext.getHashTagsTrend(filetmp) 
ext.Quit()