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
driver.get('https://www.century21.com.ve/')

#todos el inventario '//div[@class="all-listings-wrapper"]/a/text()'
inventario = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//div[@class="all-listings-wrapper"]/a')))
inventario.click() #.sendkeys('madrid')

#label pais'//*[@id="filterSidebar"]/div/div[2]/fieldset[2]/div[2]/div/button'
pais = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="filterSidebar"]/div/div[2]/fieldset[2]/div[2]/div/button')))
pais.click() #.sendkeys('madrid')

#Check box venezuela: //*[@id="react-select-14-option-0"]/input //*[@id="react-select-20-option-0"]/input //*[@id="react-select-13-option-0"]/input
#react-select-13-option-0 > input[type=checkbox] #react-select-13-option-0 > input[type=checkbox] #react-select-14-option-0 > input[type=checkbox]
check = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.CSS_SELECTOR,'#react-select-13-option-0 > input[type=checkbox]')))
check.click() 

#boton del estado /html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/fieldset[3]/div[2]/div/button
estatebutton = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/fieldset[3]/div[2]/div/button')))
estatebutton.click() 

#anzoategui /html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/fieldset[3]/div[2]/div/div[1]/div/div[2]/div/div[2]
anzoategui = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/fieldset[3]/div[2]/div/div[1]/div/div[2]/div/div[2]')))
anzoategui.click() 

#label ciudad /html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/fieldset[4]/div[2]/div/button
citylabel = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/fieldset[3]/div[2]/div/div[1]/div/div[2]/div/div[2]')))
citylabel.click()

#lecheria //*[@id="react-select-19-option-19"]/input
lecheria = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/fieldset[3]/div[2]/div/div[1]/div/div[2]/div/div[2]')))
lecheria.click()