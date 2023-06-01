from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

#Path de chromedriver
path = '/home/danel149/chromedriver'

#Opciones de chrome
options = webdriver.ChromeOptions()
##Estas linea solo para trabajar desde pdvsa
options.add_argument('--disable-extensions')
proxy = "10.172.31.3:8000"
options.add_argument('--proxy-server=%s' % proxy)

driver = webdriver.Chrome(path, chrome_options=options)

#Iniciar el navegador
driver.get('https://www.eltiempo.es/')

#WebDriverWait(driver, 60).until(ec.element_to_be_clickable(By.XPATH,'//h1[@class="title text-poppins-bold"]/a')).click()
element = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="main"]/div[4]/div/section[5]/article[2]/div/ul/li[1]/h3/a')))
element.click() #.sendkeys('madrid')
