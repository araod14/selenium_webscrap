from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import pandas as pd
import time

#Path de chromedriver
path = '/home/danel149/chromedriver'

#Opciones de chrome
options = webdriver.ChromeOptions()
##Estas linea solo para trabajar desde pdvsa
#options.add_argument('--disable-extensions')
#proxy = "10.172.31.3:8000"
#options.add_argument('--proxy-server=%s' % proxy)

driver = webdriver.Chrome(path, chrome_options=options)

#Iniciar el navegador
driver.get('https://www.swiggy.com/')

# Click ahmedabad
ahmedabad = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/div/div/div[1]/div[1]/div/ul/li[1]/a')))
ahmedabad.click()

show_more = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/main/div[9]/div/div[2]/div')))
show_more.click()

while show_more:
    show_more.click()
    #break

infor = driver.find_elements(By.XPATH, '//div[@class="sc-fmKESZ egyBvw"]')
infor.text()
    
#print(infor)

#info = 
